import numpy as np


def dijkstra(graph, s_debut, s_destination, typeMatrix=True):
    p = []

    length = graph.getOrder()
    listIds = graph.getNodeIds()

    d = (np.ones(length) * np.inf).tolist()
    d[listIds.index(s_debut)] = 0

    rg = range(0, length)
    idSommetA = s_debut
    while idSommetA != s_destination:  # and p[-1] != s_fin:
        # Choisir un sommet de plus petite distance hors de P
        indexSommetA = 0
        valueMinimum = np.inf
        for i in rg:
            if listIds[i] not in p:
                if d[i] < valueMinimum:
                    indexSommetA = i
                    valueMinimum = d[i]

        if indexSommetA == 0 and valueMinimum == np.inf:
            return [], []

        idSommetA = listIds[indexSommetA]

        # Mettre sommet A dans p
        p.append(idSommetA)

        # Voisin du sommet A
        voisins = graph.getNeighbors(idSommetA, typeMatrix=typeMatrix)
        for voisin in voisins:
            if voisin not in p and voisin != "":
                # MAJ du chemin par le voisin
                indexSommetB = listIds.index(voisin)
                idSommetB = listIds[indexSommetB]
                d[indexSommetB] = min(
                    d[indexSommetB], d[indexSommetA] + graph.getEdgeWeight(idSommetA, idSommetB)
                )

    path = [s_destination]
    newOutput = s_destination
    while newOutput != s_debut:
        neighbors = graph.getNeighbors(newOutput, typeMatrix=typeMatrix)
        listValue = []
        for neighbor in neighbors:
            if neighbor in p:
                valuePath = d[listIds.index(neighbor)]
                if valuePath < d[listIds.index(newOutput)]:
                    listValue.append(valuePath)
        if listValue:
            value = min(listValue)
            newOutput = listIds[d.index(value)]
        if path[-1] == newOutput:
            path = []
            newOutput = s_debut
        else:
            path.append(newOutput)

    path.reverse()

    return d, path

