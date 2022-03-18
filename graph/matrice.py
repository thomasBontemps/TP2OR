import numpy as np


class Matrice():

    def __init__(self, matrice=[]):
        self.__newMatrice = np.matrix(matrice)

    def viewMatrice(self):
        return self.__newMatrice

    def setMatrice(self, matrice):
        self.__newMatrice = matrice

    def newAxe(self, val):
        a, b = np.shape(self.__newMatrice)
        if val == 1:
            c = np.full(shape=(a, 1), fill_value=float('NaN'))
        else:
            c = np.full(shape=(1, b), fill_value=float('NaN'))
        self.__newMatrice = np.append(self.__newMatrice, c, axis=val)

    def delAxe(self, rg, arg):
        self.__newMatrice = np.delete(self.__newMatrice, rg, axis=arg)

    def placeVal(self, ligne, colonne, val):
        self.__newMatrice[ligne, colonne] = val
