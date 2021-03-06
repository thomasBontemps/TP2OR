from file.ReadFile import *
from graph.Graph import Graph
from utils.showGraph import showGraph
from utils.yenKSP import yenKSP
from utils.calculatedPrice import *
from utils.multiFlots import multiFlots

g = Graph(False)

nodes, links, demands = readFile(g)

#showGraph(g, nodes, links)

# Glouton
for demand in demands:
    setPriceEdge(g, links, demand.getInput(), demand.getOutput(), demand.getFlux())

#showGraph(g, nodes, links)

premiereSolution = 0
for l in links:
    premiereSolution += l.getSUCtotal()
    #print("src = ", l.getInput(), "\tOutput = ", l.getOutput(), "\t suctotal = ",l.getSUCtotal())
    l.reinitialisationSUCtotal(g)

#showGraph(g, nodes, links)

print("Le coût global de la solution est de ", round(premiereSolution, 2))

pathYenKsp = yenKSP(g, 'N01', 'N11', 2)
print("pathYenKsp =", pathYenKsp)

#showGraph(g, nodes, links)

flotProblem = multiFlots(g, links, demands)

i = 0
sommmeTotal = 0
for fp in flotProblem:
    links[i].setPIC(fp.value())
    setPriceSucTotal(links[i])
    sommmeTotal += links[i].getSUCtotal()
    i += 1

print("Avec la méthode de Pulp, nous obtenons un SUC total de :",sommmeTotal)

showGraph(g, nodes, links)
