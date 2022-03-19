from classes.Link import Link
from classes.Node import Node
from classes.Demand import Demand


def readFile(g):
    # Lecture du fichier
    file = open("file/network_instance.txt", "r")
    lignes = file.readlines()

    # Suppresion des lignes inutiles
    lignes = [i for i in lignes if i != '\n']
    lignes = [i for i in lignes if i[0] != '#']
    lignes = [i for i in lignes if i[0] != '?']

    # Creation des listes
    listNodes = []
    listDemands = []
    listLinks = []

    # Séparation des lignes pour retrouver des chaines logiques
    i = lignes.pop(0)
    i = lignes.pop(0)
    while i[0] != ')':  # Nodes
        values = i.split(" ")
        listNodes.append(Node(values[2], float(values[4]), float(values[5])))
        g.addNode(values[2])
        i = lignes.pop(0)

    i = lignes.pop(0)
    i = lignes.pop(0)
    while i[0] != ')':  # Links
        values = i.split(" ")
        l = Link(values[2], values[4], values[5], float(values[7]), float(values[8]), float(values[9]),
                 float(values[10]), float(values[12]), float(values[13]))
        listLinks.append(l)
        g.addEdge(values[4], values[5], float(values[10])*3)  # mettre le set-up cost total pour avoir le chemin le plus court
        g.addEdge(values[4], values[5], float(values[10])*3, typeMatrix=False)  # mettre le set-up cost total pour avoir le chemin le plus court
        i = lignes.pop(0)

    i = lignes.pop(0)
    i = lignes.pop(0)
    while i[0] != ')':  # Demands
        d = i.split(' ')
        listDemands.append(Demand(d[4], d[5], d[8]))
        i = lignes.pop(0)

    return listNodes, listLinks, listDemands
