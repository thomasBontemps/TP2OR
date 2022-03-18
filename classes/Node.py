
class Node:
    def __init__(self, id, x = 0, y = 0):
        self.__id = id
        self.__positionX = x
        self.__positionY = y

    def getId(self):
        return self.__id

    def getPositionX(self):
        return self.__positionX

    def getPositionY(self):
        return self.__positionY

    def setId(self, id):
        self.__id = id

    def setPositionX(self, positionX):
        self.__positionX = positionX

    def setPositionY(self, positionY):
        self.__positionY = positionY
