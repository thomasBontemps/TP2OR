from file.ReadFile import *
from graph.Graph import Graph
from utils.showGraph import showGraph
from utils.yenKSP import yenKSP
from utils.calculatedPrice import *
from utils.multiFlots import multiFlots

g = Graph(False)

nodes, links, demands = readFile(g)

listIds = g.getNodeIds()

for demand in demands:
    setPriceEdge(g, links, demand.getInput(), demand.getOutput(), demand.getFlux())

#showGraph(g, nodes, links)

premiereSolution = 0
for l in links:
    premiereSolution += l.getSUCtotal()
    #print("src = ", l.getInput(), "\tOutput = ", l.getOutput(), "\t suctotal = ",l.getSUCtotal())
    #l.reinitialisationSUCtotal(g)

print("Le coût global de la solution est de ", round(premiereSolution, 2))

pathYenKsp = yenKSP(g, 'N01', 'N19', 30)
print("pathYenKsp =", pathYenKsp)

#showGraph(g, nodes, links)

flotProblem = multiFlots(g, links, demands)

i = 0
sommmeTotal = 0
for fp in flotProblem:
    sommmeTotal += getVal(links[i].getSUC(), fp.value())
    i += 1

print(flotProblem)
print(len(flotProblem))
print(sommmeTotal)



