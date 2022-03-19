import pulp


def multiFlots(graphe, links):
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
