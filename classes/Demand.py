
class Demand:
    def __init__(self, input, output, flux):
        self.__input = input
        self.__output = output
        self.__flux = flux

    def getInput(self):
        return self.__input

    def getOutput(self):
        return self.__output

    def getFlux(self):
        return self.__flux
