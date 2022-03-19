import math
from utils.dijkstra import dijkstra


def setPriceSucTotal(l):
    val = l.getPIC()
    suc = l.getSUC()
    if 0 < val <= 200:
        l.setSUCtotal(suc + 2 * suc)
    elif 200 < val <= 800:
        total = 8 * suc
        l.setSUCtotal(total - 0.1 * total)
    elif 800 < val <= 1600:
        total = 16 * suc
        l.setSUCtotal(total - 0.15 * total)
    else:
        k = round(math.log2(val / 1600))
        total = 32 * suc
        sucTotal = math.pow(2, k) * (total - 0.25 * total)
        l.setSUCtotal(sucTotal)


def setPriceEdge(g, links, input, output, flux):
    _, path = dijkstra(g, input, output, links)

    rg = range(0, len(path) - 1)
    for i in rg:
        for l in links:
            if (l.getInput() == path[i] or l.getInput() == path[i + 1]) and (
                    l.getOutput() == path[i] or l.getOutput() == path[i + 1]):
                l.setPIC(l.getPIC() + flux)
                setPriceSucTotal(l)
