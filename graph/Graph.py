import numpy as np
from graph.matrice import Matrice


class Graph:
    """Graph implementation based on adjacency matrix"""

    def __init__(self, directed=False):
        """Initializes the graph (undirected by default)."""
        self.__directed = directed
        self.__matriceEdgeSUC = Matrice()
        self.__matriceEdgeSUC_previous = Matrice()
        self.__listeNode = []
        self.__listeVal = []

    def getOrder(self):
        return len(self.__listeNode)

    def isDirected(self):
        return self.__directed

    def getNodeIds(self):
        """Returns the identifiers of nodes in the graph, as a Python list of integers."""
        return self.__listeNode

    def getMatriceSUC(self):
        """Returns the identifiers of nodes in the graph, as a Python list of integers."""
        return self.__matriceEdgeSUC.viewMatrice()

    def getMatriceSUC_previous(self):
        """Returns the identifiers of nodes in the graph, as a Python list of integers."""
        return self.__matriceEdgeSUC_previous.viewMatrice()

    # ----------- Nodes operations ---------------------- #

    def addNode(self, id, value=None):
        """Adds the node identified by id in the graph, with default value None. Returns True on success, False otherwise."""
        if id in self.__listeNode:
            return False
        else:
            self.__listeNode.append(id)
            self.__listeVal.append(value)
            self.__matriceEdgeSUC.newAxe(1)
            self.__matriceEdgeSUC.newAxe(0)
            self.__matriceEdgeSUC_previous.newAxe(1)
            self.__matriceEdgeSUC_previous.newAxe(0)
            return True

    def removeNode(self, id):
        """Removes the node identified by id in the graph. Returns True on success, False otherwise."""
        if id in self.__listeNode:
            indexId = self.__listeNode.index(id)
            self.__listeNode.remove(id)
            del self.__listeVal[indexId]
            self.__matriceEdgeSUC.delAxe(indexId, 1)
            self.__matriceEdgeSUC.delAxe(indexId, 0)
            self.__matriceEdgeSUC_previous.delAxe(indexId, 1)
            self.__matriceEdgeSUC_previous.delAxe(indexId, 0)
            return True
        return False

    def getNodeValue(self, id):
        """Returns the value of the node identified by id in the graph (None if the specified node does not exist)."""
        if id in self.__listeNode:
            return self.__listeVal[self.__listeNode.index(id)]
        return None

    def setNodeValue(self, id, value):
        """Sets the value of the node identified by id in the graph to the specified one. Returns True on success, False otherwise."""
        if id in self.__listeNode:
            self.__listeVal[self.__listeNode.index(id)] = value
            return True
        return False

    def getNeighbors(self, id, typeMatrix=True):
        """Returns the identifiers of nodes in the neighborhood of the node identified by id. Returns a Python list of integers on success, None otherwise."""
        if typeMatrix:
            x = self.__matriceEdgeSUC
        else:
            x = self.__matriceEdgeSUC_previous
        if id in self.__listeNode:
            listNeighbor = x.viewMatrice().tolist()
            listNeighbor = listNeighbor[self.__listeNode.index(id)]
            placeNeighbor = []
            positionNeighbor = []
            neighbor = []
            for val in listNeighbor:
                if not np.isnan(val):
                    placeNeighbor.append(val)
            for valNone in placeNeighbor:
                positionNeighbor.append(listNeighbor.index(valNone))
                listNeighbor[listNeighbor.index(valNone)] = np.nan
            for position in positionNeighbor:
                neighbor.append(self.__listeNode[position])
            return neighbor
        return None

    # ----------- Edges operations ---------------------- #

    def reinitialisationMatrix(self, typeMatrix=True):
        """Permit to reinitialise the matrix by an another"""
        if typeMatrix:
            self.__matriceEdgeSUC = Matrice(self.getMatriceSUC_previous())
        else:
            self.__matriceEdgeSUC_previous = Matrice(self.getMatriceSUC())

    def addEdge(self, sourceId, targetId, weight=1, typeMatrix=True):
        """Adds an edge between the nodes identified by sourceId and targetId in the graph, with default weight 1. Returns True on success, False otherwise."""
        if (sourceId in self.__listeNode) and (targetId in self.__listeNode):
            sourceId = self.__listeNode.index(sourceId)
            targetId = self.__listeNode.index(targetId)
            if typeMatrix:
                x = self.__matriceEdgeSUC
            else:
                x = self.__matriceEdgeSUC_previous
            if np.isnan(x.viewMatrice()[sourceId, targetId]):
                x.placeVal(sourceId, targetId, weight)
                if not self.__directed:
                    x.placeVal(targetId, sourceId, weight)
                return True
            return False
        return False

    def removeEdge(self, sourceId, targetId, weight=np.nan, typeMatrix=True):
        """Removes the edge between the nodes identified by sourceId and targetId in the graph. Returns True on success, False otherwise."""
        if (sourceId in self.__listeNode) and (targetId in self.__listeNode):
            sourceId = self.__listeNode.index(sourceId)
            targetId = self.__listeNode.index(targetId)
            if typeMatrix:
                x = self.__matriceEdgeSUC
            else:
                x = self.__matriceEdgeSUC_previous
            x.placeVal(sourceId, targetId, weight)
            if not self.__directed:
                x.placeVal(targetId, sourceId, weight)
            return True
        return False

    def getEdgeWeight(self, sourceId, targetId, typeMatrix=True):
        """Returns the weight of the edge between the nodes identified by sourceId and targetId in the graph (None if the specified edge does not exist)."""
        if (sourceId in self.__listeNode) and (targetId in self.__listeNode):
            if typeMatrix:
                edge = self.__matriceEdgeSUC.viewMatrice()[
                    self.__listeNode.index(sourceId), self.__listeNode.index(targetId)]
            else:
                edge = self.__matriceEdgeSUC_previous.viewMatrice()[
                    self.__listeNode.index(sourceId), self.__listeNode.index(targetId)]
            if np.isnan(edge):
                return None
            return edge
        return None

    def setEdgeWeight(self, sourceId, targetId, weight,
                      typeMatrix=True):  # newEdge is an additional argument to make the difference between existing and new edge
        """Sets the weight of the edge between the nodes identified by sourceId and targetId in the graph to the specified one. Returns True on success, False otherwise."""
        if (sourceId in self.__listeNode) and (targetId in self.__listeNode):
            sourceId = self.__listeNode.index(sourceId)
            targetId = self.__listeNode.index(targetId)
            if typeMatrix:
                x = self.__matriceEdgeSUC
            else:
                x = self.__matriceEdgeSUC_previous
            if np.isnan(x.viewMatrice()[sourceId, targetId]) == False:
                x.placeVal(sourceId, targetId, weight)
                if self.__directed != True:
                    x.placeVal(targetId, sourceId, weight)
                return True
            return False
        return False
