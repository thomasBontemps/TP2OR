import pulp
from utils.yenKSP import yenKSP
import numpy as np
from utils.showGraph import showGraph


def multiFlots(graphe, links, demands, nodes):

    for demand in demands:
        # Calculate k-shortest path
        paths = yenKSP(graphe, demand.getInput(), demand.getOutput())





    setupCostTotalList = [l.getSUCtotal() for l in links]

    W = {}

    setupCostTotal = pulp.LpVariable.dicts("setupCostTotal", setupCostTotalList, lowBound=0, cat="Continuous")

    flotProblem = pulp.LpProblem("MultiFlots", pulp.LpMinimize)

    flotProblem += (
        pulp.lpSum(
            setupCostTotal
        ),
        "Total_cost"
    )

    # Definition of the constraints
    flotProblem += sum([l.getPIC() for l in links]) == sum([d.getFlux() for d in demands]), "flow"

    flotProblem.solve()
    print("Status : ", pulp.LpStatus[flotProblem.status])

    return -1


