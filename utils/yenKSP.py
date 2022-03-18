from utils.dijkstra import *
from classes.Node import Node


def yenKSP(graph, source, sink, K=5):
    # Determine the shortest path from the source to the sink.
    # Stock all k-shortest beginning by dijkstra of source and destination
    _, littlePathSourceId = dijkstra(graph, source, sink)
    paths = [littlePathSourceId]

    rg = 1
    k = 0
    while rg < K:
        # The spur node ranges from the first node to the next to last node in the previous k-shortest path.
        lengthPaths = range(1, len(paths[k])-1)

        for i in lengthPaths:
            if i ==3:
                print("ok")
            startPath = [idNode for idNode in paths[k][:i]]
            matrice = graph.getMatriceSUC_previous()
            neighbors = graph.getNeighbors(startPath[-1])
            for neighbor in neighbors:
                if neighbor not in startPath:
                    # Get little path from neighbors
                    # Delete weight between node A(neighbor) and B(destination)
                    graph.removeEdge(startPath[-1], neighbor, np.nan, False)
                    _, path = dijkstra(graph, neighbor, sink, typeMatrix=False)


                    # If path doesn't exist, add to paths
                    newPath = startPath + path
                    if newPath not in paths:
                        if False not in [True if newPath.count(i) == 1 else False for i in newPath]:
                            paths.insert(rg, newPath)
                            rg += 1

                if rg == K:
                    graph.reinitialisationMatrix(False)
                    return paths
            graph.reinitialisationMatrix(False)
            if rg == K:
                return paths

        graph.reinitialisationMatrix()
        k += 1
    return paths