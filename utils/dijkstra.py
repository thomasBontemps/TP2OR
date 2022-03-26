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
    path = littlePath(graph, s_debut, listIds, p, d)

    return d, path


# Retourne la distance entre chaque noeud par rapport à au début
def allIdPath(graph, s_debut, s_destination, listIds, typeMatrix):
    length = graph.getOrder()

    p = []

    d = (np.ones(length) * np.inf).tolist()
    d[listIds.index(s_debut)] = 0

    rg = range(0, length)
    idSommetA = s_debut
    listTupleLink = [(None, idSommetA)]
    while idSommetA != s_destination:
        # Choisir un sommet de plus petite distance hors de P
        indexSommetA = 0
        valueMinimum = np.inf
        myListNode = [tupleP[1] for tupleP in p]
        for i in rg:
            if listIds[i] not in myListNode:
                if d[i] <= valueMinimum:
                    indexSommetA = i
                    valueMinimum = d[i]

        # Eviter les boucles infinies s'il n'y a pas de voisins
        if indexSommetA == 0 and valueMinimum == np.inf:
            return [], []

        idSommetA = listIds[indexSommetA]

        # Mettre sommet A dans p
        for tupleLink in listTupleLink:
            if tupleLink[1] == idSommetA:
                p.append(tupleLink)
                listTupleLink.remove(tupleLink)
        if idSommetA == s_destination:
            return d, p

        # Voisin du sommet A
        voisins = graph.getNeighbors(idSommetA, typeMatrix=typeMatrix)
        for voisin in voisins:
            if voisin not in p and voisin != "":
                # MAJ du chemin par le voisin
                indexSommetB = listIds.index(voisin)
                d[indexSommetB] = min(
                    d[indexSommetB], d[indexSommetA] + graph.getEdgeWeight(idSommetA, voisin)
                )
                newTupleLink = (idSommetA, voisin)
                if newTupleLink not in listTupleLink:
                    listTupleLink.append(newTupleLink)
    return d, p


# Récupérer le plus petit chemin entre le début et la destination par rapport à la nouvelle liste créée
def littlePath(graph, s_debut, listIds, p, d):
    path = []
    if p:
        lengthP = len(p)
        newOutput = p[-1]
        path = [newOutput[1]]
        idxLittleNeighbor = 0
        while newOutput[0] is not None:
            if idxLittleNeighbor < lengthP:
                tupleNextInputOutput = p[idxLittleNeighbor]
                if tupleNextInputOutput[1] == newOutput[0]:
                    if tupleNextInputOutput[0] is not None:
                        if d[listIds.index(newOutput[0])] == (d[listIds.index(tupleNextInputOutput[0])] + graph.getEdgeWeight(tupleNextInputOutput[0], tupleNextInputOutput[1])):
                            newOutput = tupleNextInputOutput
                            path.append(newOutput[1])
                            idxLittleNeighbor = 0
                        else:
                            idxLittleNeighbor += 1
                    else:
                        newOutput = tupleNextInputOutput
                        path.append(newOutput[1])
                        idxLittleNeighbor = 0
                else:
                    idxLittleNeighbor += 1
            else:
                newOutput = p[-2]
                path = [newOutput[-2]]
                idxLittleNeighbor = 0

        path.reverse()
    return path
