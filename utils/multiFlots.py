import pulp
from utils.yenKSP import yenKSP
import numpy as np
from utils.calculatedPrice import getVal
from utils.showGraph import showGraph


def multiFlots(graphe, links, demands):
    lengthLinks = len(links)
    rangeLinks = range(0, lengthLinks)

    capaciteList = [i for i in rangeLinks]

    X = pulp.LpVariable.dicts("X", capaciteList, lowBound=0, cat="Continuous")

    flotProblem = pulp.LpProblem("MultiFlots", pulp.LpMinimize)

    flotProblem += (
        pulp.lpSum(
            [getVal(l.getSUC(), X[links.index(l)]) for l in links]
        ),
        "Total_cost"
    )

    # Definition of the constraints

    N = []
    flux = []
    for demand in demands:
        # Calculate k-shortest path
        N_prime = np.zeros(lengthLinks)
        N_prime_bis = []
        paths = yenKSP(graphe, demand.getInput(), demand.getOutput())
        for path in paths:
            rangePath = range(0, len(path) - 1)
            for i in rangePath:
                for link in links:
                    if (link.getInput() == path[i] or link.getInput() == path[i + 1]) and (
                            link.getOutput() == path[i] or link.getOutput() == path[i + 1]):
                        N_prime[links.index(link)] += 1  # Determine how many times branch it uses for this demand
                        N_prime_bis += X[links.index(link)]
        N.append(N_prime)

        # Create a list that contain each variable uses multiply by n time
        listX = []
        rangeN_prime = range(0, len(N_prime))
        for i in rangeN_prime:
            listX.append(N_prime[i] * X[i])

        # Contrainte 1 : sum(pi) >= flux ; The sum of all path for this demand should contain flow of this demand
        flotProblem += pulp.lpSum(listX) >= demand.getFlux(), "demande_" + str(demands.index(demand))

        flux.append(demand.getFlux())

    # Finds max flow of a weight
    listCapaciteFlux = [[X[i], 0, np.inf] for i in rangeLinks]
    rangeN = range(0, len(N))
    for i in rangeN:
        for j in rangeLinks:
            # If multiplication superior of 0 --> fluxMax = fluxPrecedent += fluxOfDemandI
            if N[i][j] > 0:
                listCapaciteFlux[j][1] += flux[i]
            if listCapaciteFlux[j][2] > flux[i]:
                listCapaciteFlux[j][2] = flux[i]

    for tupleCapaciteFlux in listCapaciteFlux:
        print(str(tupleCapaciteFlux[0]))
        # Contrainte 2 : sum(capacité d'une arête) <= sum(flux totaux passant par cette arête)
        flotProblem += tupleCapaciteFlux[0] <= tupleCapaciteFlux[1], "capaciteMax_" + str(tupleCapaciteFlux[0])

        # Contrainte : une arrete >= fluxMinimum
        flotProblem += tupleCapaciteFlux[0] >= tupleCapaciteFlux[2], "capaciteMinimum_" + str(tupleCapaciteFlux[0])

    # Contrainte 3 : Ensemble des poids doit être égale au flux de chaque demand
    flotProblem += pulp.lpSum(X) == sum(flux), "Flux"



    # Solve the problem
    flotProblem.solve()

    # return variable calculated by the system
    return X.values()
