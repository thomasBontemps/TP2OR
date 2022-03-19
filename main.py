from file.ReadFile import *
from graph.Graph import Graph
from utils.showGraph import showGraph
from utils.dijkstra import *
from utils.yenKSP import yenKSP
from utils.calculatedPrice import *

g = Graph(False)

nodes, links, demands = readFile(g)

listIds = g.getNodeIds()


listPaths = []
for demand in demands:
    d = demand.split(' ')

    input = d[4]
    output = d[5]

    flux = float(d[8])
    setPriceEdge(g, links, input, output, flux)


g.reinitialisationMatrix()

premiereSolution = 0
for l in links:
    premiereSolution += l.getSUCtotal()

print("Le coût global de la solution est de ", round(premiereSolution, 2))

pathYenKsp = yenKSP(g, 'N01', 'N19', 30)
print("pathYenKsp =", pathYenKsp)



