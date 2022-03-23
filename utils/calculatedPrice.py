import math
from utils.dijkstra import dijkstra


# Permet de calculer le SUC total à partir du SUC et d'une valeur de la branche
def getVal(suc, val):
    if val == 0:
        return 0
    elif 0 < val <= 200:
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


# Permet d'affecter la nouvelle valeur du SUC total en fonction du SUC et de la capatacité du lien
def setPriceSucTotal(l):
    val = l.getPIC()
    suc = l.getSUC()
    l.setSUCtotal(getVal(suc, val))


# Permet d'ajouter un flux à une branche par rapport au plus court chemin entre l'input et l'output
def setPriceEdge(g, links, input, output, flux):
    _, path = dijkstra(g, input, output, links)

    rg = range(0, len(path) - 1)
    for i in rg:
        for l in links:
            if (l.getInput() == path[i] or l.getInput() == path[i + 1]) and (
                    l.getOutput() == path[i] or l.getOutput() == path[i + 1]):
                l.setPIC(l.getPIC() + flux)
                setPriceSucTotal(l)
