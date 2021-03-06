import pulp
from utils.yenKSP import yenKSP
import numpy as np
from utils.calculatedPrice import getVal
from utils.showGraph import showGraph


def multiFlots(graphe, links, demands):
    lengthLinks = len(links)
    rangeLinks = range(0, lengthLinks)

    capaciteList = [i for i in rangeLinks]
    capaciteNode = pulp.LpVariable.dicts("capaciteNode", capaciteList, lowBound=1, cat="Continuous")

    sucTotalList = [getVal(l.getSUC(), capaciteNode[links.index(l)]) for l in links]
    sucTotalNode = pulp.LpVariable.dicts("sucTotalNode", sucTotalList, lowBound=0, cat="Continuous")

    flotProblem = pulp.LpProblem("MultiFlots", pulp.LpMinimize)

    flotProblem += (
        pulp.lpSum(
            sucTotalList  # = SUC_total
        ),
        "Total_cost"
    )

    # Definition of the constraints

    N = []
    flux = []
    for demand in demands:
        # Calculate k-shortest path
        N_prime = np.zeros(lengthLinks)
        paths = yenKSP(graphe, demand.getInput(), demand.getOutput(),1)
        for path in paths:
            N_prime_bis = []
            rangePath = range(0, len(path) - 1)
            for i in rangePath:
                for link in links:
                    if (link.getInput() == path[i] or link.getInput() == path[i + 1]) and (
                            link.getOutput() == path[i] or link.getOutput() == path[i + 1]):
                        N_prime[links.index(link)] += 1  # Determine how many times link it uses for this demand
                        N_prime_bis += capaciteNode[links.index(link)]
                flotProblem += N_prime_bis >= demand.getFlux()
        N.append(N_prime)

        # Create a list that contain each variable uses multiply by n time
        listCapaciteNode = []
        rangeN_prime = range(0, len(N_prime))
        for i in rangeN_prime:
            listCapaciteNode.append(N_prime[i] * capaciteNode[i])

        # Contrainte 1 : sum(pi) == flux ; The sum of all path for this demand should contain flow of this demand
        flotProblem += listCapaciteNode[-1] == demand.getFlux(), "demande_" + str(demands.index(demand))

        flux.append(demand.getFlux())

    # Finds max flow of a weight
    listCapaciteFlux = [[capaciteNode[i], 0, np.inf, 0] for i in rangeLinks]
    rangeN = range(0, len(N))
    for i in rangeN:
        for j in rangeLinks:
            # If multiplication superior of 0 --> fluxMax = fluxPrecedent += fluxOfDemandI
            if N[i][j] > 0:
                listCapaciteFlux[j][1] += flux[i]
            if listCapaciteFlux[j][2] > flux[i]:
                listCapaciteFlux[j][2] = flux[i]
            if listCapaciteFlux[j][3] > flux[i]:
                listCapaciteFlux[j][3] = flux[i]

    for tupleCapaciteFlux in listCapaciteFlux:
        # Contrainte 2 : sum(capacit?? d'une ar??te) <= sum(flux totaux passant par cette ar??te)
        flotProblem += tupleCapaciteFlux[0] <= tupleCapaciteFlux[1], "capaciteMax_" + str(tupleCapaciteFlux[0])
        #flotProblem += tupleCapaciteFlux[0] >= 1, "positivite" + str(tupleCapaciteFlux[0])
        print(tupleCapaciteFlux)
        flotProblem += tupleCapaciteFlux[0] >= tupleCapaciteFlux[2], "min" + str(tupleCapaciteFlux[0])
        pass


    # Contrainte 3 : Ensemble des poids doit ??tre ??gale au flux de chaque demand
    #flotProblem += pulp.lpSum(capaciteNode) >= sum(flux), "Flux"



    # Solve the problem
    flotProblem.solve()
    if pulp.value(flotProblem.objective) is not None:
        # return variable calculated by the system
        pass
    return capaciteNode.values()

