from file.ReadFile import *
from graph.Graph import Graph
from utils.showGraph import showGraph
from utils.dijkstra import *
from utils.yenKSP import yenKSP
from utils.calculatedPrice import *

g = Graph(False)

nodes, links, demands = readFile(g)

listIds = g.getNodeIds()

showGraph(g, nodes, links)

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
                setPriceSucTotal(l)
<<<<<<< HEAD

showGraph(g, nodes, links)
=======
                g.removeEdge(l.getInput(), l.getOutput(), weight=l.getSUCtotal())

showGraph(g, nodes, links)
g.reinitialisationMatrix(False)
showGraph(g, nodes, links)
>>>>>>> 8d3bf9e2e7803c1c869eac91683c959b4ee4cea0

premiereSolution = 0
for l in links:
    print(l.getSUCtotal())
    premiereSolution += l.getSUCtotal()

print("Le coût global de la solution est de ", round(premiereSolution, 2))

pathYenKsp = yenKSP(g, 'N01', 'N19', 30)
print("pathYenKsp =", pathYenKsp)

showGraph(g, nodes, links)
