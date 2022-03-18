from file.ReadFile import *
from graph.Graph import Graph
from classes.Node import Node
from classes.Link import Link
from utils.showGraph import showGraph
from utils.dijkstra import *
from utils.yenKSP import yenKSP
import numpy as np
import matplotlib.pyplot as plt

g = Graph(False)

nodes, links, demands = readFile(g)

listIds = g.getNodeIds()

listPaths = []
for demand in demands:
    d = demand.split(' ')

    input = d[4]
    output = d[5]

    flux = float(d[8])

    _, path = dijkstra(g, input, output)

    rg = range(0, len(path) - 1)
    for i in rg:
        for l in links:
            if (l.getInput() == path[i] or l.getInput() == path[i + 1]) and (l.getOutput() == path[i] or l.getOutput() == path[i + 1]):
                l.setPIC(l.getPIC() + flux)

for l in links:
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
        total = 32 * suc
        sucTotal = total - 0.25 * total
        if 1600 < val <= 3200:
            l.setSUCtotal(sucTotal)
        else:
            l.setSUCtotal(2 * sucTotal)

premiereSolution = 0
for l in links:
    premiereSolution += l.getSUCtotal()

print("Le coût global de la solution est de ", round(premiereSolution, 2))

pathYenKsp = yenKSP(g, 'N01', 'N19', 6)
print("pathYenKsp =", pathYenKsp)

showGraph(g, nodes, links)
A = g.getMatriceSUC_previous()
AA = g.getMatriceSUC()
print("tototo")

