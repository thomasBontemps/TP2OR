import numpy as np
from utils.showGraph import showGraph


# Récupérer le plus petit chemin
def dijkstra(graph, s_debut, s_destination, typeMatrix=True):

    # Récupération de la liste des noeuds du graphe
    listIds = graph.getNodeIds()

    # d : Distance entre chaque noeud par rapport au noeud début jusqu'au noeud de fin
    # p : Liste des noeuds utilisés par le path
    d, p = allIdPath(graph, s_debut, s_destination, listIds, typeMatrix)

    # Récupérer le plus petit path
    path = littlePath(graph, s_debut, s_destination, listIds, d, p, typeMatrix)

    return d, path


# Retourne la distance entre chaque noeud par rapport à au début
def allIdPath(graph, s_debut, s_destination, listIds, typeMatrix):
    length = graph.getOrder()

    p = []

    d = (np.ones(length) * np.inf).tolist()
    d[listIds.index(s_debut)] = 0

    rg = range(0, length)
    idSommetA = s_debut
    while idSommetA != s_destination:
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
    return d, p


# Récupérer le plus petit chemin entre le début et la destination par rapport à la nouvelle liste créée
def littlePath(graph, s_debut, s_destination, listIds, d, p, typeMatrix):
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
    return path
