import matplotlib.pyplot as plt
import numpy as np


def showGraph(graph, nodes, links, typeMatrix=True):
    fig, ax = plt.subplots()
    if typeMatrix:
        matrice = np.asarray(graph.getMatriceSUC())  # Get matrix of connection between each node
    else:
        matrice = np.asarray(graph.getMatriceSUC_previous())  # Get matrix of connection between each node
    ids = graph.getNodeIds()  # Get all nodes
    rg = range(0, graph.getOrder())
    x = []
    y = []
    tuplesDirected = []
    for i in rg:
        # Get coordinate of each node
        x.append(nodes[i].getPositionX())
        y.append(nodes[i].getPositionY())
        for j in rg:
            if not np.isnan(matrice[i][j]):
                # If there is a value, keep node in a tuple
                tuplesDirected.append((ids[i], ids[j]))

    ax.scatter(x, y, edgecolor='r')

    for i, txt in enumerate(ids):
        ax.annotate(txt, (x[i], y[i]), fontsize=8, horizontalalignment='right', verticalalignment='bottom',
                    color='r')  # Add node value in each point of graphs

    for tuple in tuplesDirected:
        # Get the position of link between node A and B
        axeX = [nodes[ids.index(tuple[0])].getPositionX(), nodes[ids.index(tuple[1])].getPositionX()]
        axeY = [nodes[ids.index(tuple[0])].getPositionY(), nodes[ids.index(tuple[1])].getPositionY()]
        label = ''
        for l in links:
            if (l.getInput() == tuple[0] or l.getInput() == tuple[1]) and (
                    l.getOutput() == tuple[0] or l.getOutput() == tuple[1]):  # Find which link correspond to node A and B
                label = str(int(l.getSUCtotal()))
        plt.plot(axeX, axeY, c='black', linewidth=1)  # Create line between node A to B
        plt.text((axeX[0] + axeX[1]) / 2, (axeY[0] + axeY[1]) / 2, label, fontsize=9, horizontalalignment='center',
                 verticalalignment='center')  # Add value of SUC
    plt.show()
