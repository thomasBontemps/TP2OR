
class Link:
    def __init__(self, id, input, output, pre_installed_capacity, pre_installed_capacity_cost, routing_cost, setup_cost, module_capacity, module_cost):
        self.__id = id
        self.__input = input
        self.__output = output
        self.__pic = pre_installed_capacity
        self.__pic_cost = pre_installed_capacity_cost
        self.__routing_cost = routing_cost
        self.__suc = setup_cost
        self.__module_capacity = module_capacity
        self.__module_cost = module_cost
        self.__sucTotal = setup_cost * 3

    def getId(self):
        return self.__id

    def getInput(self):
        return self.__input

    def getOutput(self):
        return self.__output

    def getPIC(self):
        return self.__pic

    def getPICcost(self):
        return self.__pic_cost

    def getRoutingCost(self):
        return self.__routing_cost

    def getSUC(self):
        return self.__suc

    def getSUCtotal(self):
        return self.__sucTotal

    def getModuleCapacity(self):
        return self.__module_capacity

    def getModuleCost(self):
        return self.__module_cost

    def setPIC(self,pic):
        self.__pic = pic

    def setPICcost(self, picCost):
        self.__pic_cost = picCost

    def setRoutingCost(self, rc):
        self.__routing_cost = rc

    def setSUC(self, suc):
        self.__suc = suc

    def setSUCtotal(self, suc):
        self.__sucTotal = suc

    def setModuleCapacity(self, mc):
        self.__module_capacity = mc

    def setModuleCost(self, mc):
        self.__module_cost = mc

    def reinitialisationSUCtotal(self, graph):
        """Permet de réinitialiser les valeurs servant à calculer le SUC_total / Dans ce cas, l'ajout du graphe permet de réinitialiser les poids entre l'input et l'output"""
        self.__sucTotal = self.__suc + 2 * self.__suc
        self.__pic = 0
        graph.removeEdge(self.__input, self.__output, self.__sucTotal)
