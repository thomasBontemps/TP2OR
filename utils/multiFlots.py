import pulp
from utils.yenKSP import yenKSP
import numpy as np
from utils.calculatedPrice import getVal
from utils.showGraph import showGraph


def multiFlots(graphe, links, demands, nodes):

    capaciteList = [l.getPIC() for l in links]
    setupCostTotalList = [l.getSUCtotal() for l in links]

    X = pulp.LpVariable.dicts("x", capaciteList, lowBound=0, cat="Continuous")

    flotProblem = pulp.LpProblem("MultiFlots", pulp.LpMinimize)

    flotProblem += (
        pulp.lpSum(
            setupCostTotalList
        ),
        "Total_cost"
    )

    # Definition of the constraints

    lengthLinks = len(links)
    rangeLinks = range(0, lengthLinks)

    N = []
    flux = []
    for demand in demands:
        # Calculate k-shortest path
        N_prime = np.zeros(lengthLinks)
        paths = yenKSP(graphe, demand.getInput(), demand.getOutput())
        for path in paths:
            rangePath = range(0,len(path)-1)
            for i in rangePath:
                for link in links:
                    if (link.getInput() == path[i] or link.getInput() == path[i + 1]) and (
                            link.getOutput() == path[i] or link.getOutput() == path[i + 1]):
                        N_prime[links.index(link)] += 1
        N.append(N_prime)
        listX = []
        rangeN_prime = range(0, len(N_prime))
        for i in rangeN_prime:
            multiplicity = N_prime[i]
            if multiplicity > 0:
                listX.append(multiplicity * X[links[i].getPIC()])

        # Contrainte 1 : sum(pi) >= flux
        flotProblem += pulp.lpSum(listX) >= demand.getFlux(), "demande_" + str(demands.index(demand))

        flux.append(demand.getFlux())

    # Contrainte 2 : sum(capacité d'une arrete) <= sum(flux totaux passant par cette arrête
    listCapaciteFlux = [ [X[l.getPIC()], 0] for l in links]

    rangeN = range(0, len(N))

    for i in rangeN:
        for j in rangeLinks:
            if N[i][j] > 0:
                listCapaciteFlux[j][1] += flux[i]

    for tupleCapaciteFlux in listCapaciteFlux:
        flotProblem += tupleCapaciteFlux[0] <= tupleCapaciteFlux[1]

    flotProblem.solve()
    print("Status : ", pulp.LpStatus[flotProblem.status])

    # OUTPUT
    print("Solution flot :")
    demande = "demande: "
    print(X)
    for x in X.values():
        demande += str(x.value()) + ", "
    print(demande)

    return X.values()


