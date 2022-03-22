import math
from utils.dijkstra import dijkstra


def getVal(suc, val):
    if 0 < val <= 200:
        return suc + 2 * suc
    elif 200 < val <= 800:
        total = 8 * suc
        return total - 0.1 * total
    if 800 < val <= 1600:
        total = 16 * suc
        return total - 0.15 * total
    else:
        k = round(math.log2(val / 1600))
        total = 32 * suc
        sucTotal = math.pow(2, k) * (total - 0.25 * total)
        return sucTotal




def setPriceSucTotal(l):
    val = l.getPIC()
    suc = l.getSUC()
    l.setSUCtotal(getVal(suc, val))


def setPriceEdge(g, links, input, output, flux):
    _, path = dijkstra(g, input, output, links)

    rg = range(0, len(path) - 1)
    for i in rg:
        for l in links:
            if (l.getInput() == path[i] or l.getInput() == path[i + 1]) and (
                    l.getOutput() == path[i] or l.getOutput() == path[i + 1]):
                l.setPIC(l.getPIC() + flux)
                setPriceSucTotal(l)
