import pulp
from utils.yenKSP import yenKSP


def multiFlots(graphe, links, demands):

    for demand in demands:
        paths = yenKSP(graphe, demand.getInput(), demand.getOutput())
        print(paths)

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

    return -1
