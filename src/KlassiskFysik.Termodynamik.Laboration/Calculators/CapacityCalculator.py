import csv
import numpy as np
from Calculators.TemperatureCalculator import TemperatureCalculator

class CapacityCalculator(TemperatureCalculator):

    def __init__(self, settings):
        super(CapacityCalculator, self).__init__(settings)

    def CalculateCapacity(self, current, mass, adjustment, avgCooling):
        self._capacityCalculations = list()
        self.CalculateTemperatures()

        for temp in self._temperatures:
            time = temp[0];
            timeInterval = temp[1];
            temperatureDiff = temp[2] + temp[2]*avgCooling

            heat = current * current * self.settings.impedance * timeInterval

            C = heat / temperatureDiff
            adjustedC = C - adjustment
            cp = adjustedC / mass

            self._capacityCalculations.append([time, timeInterval, temperatureDiff, heat, C, adjustedC, cp])

            #print("------------")
            #print(self._capacityCalculations)
            #print("------------")

    def MeanSpecificHeat(self):
        return np.mean(self.GetSpecificHeats()[:,1])

    def MeanHeatCapacity(self):
        return np.mean(self.GetHeatCapacities()[:,1])

    def GetSpecificHeats(self):
        capacities = [[row[0], row[6]] for row in self._capacityCalculations]

        return np.array(capacities)

    def GetHeatCapacities(self):
        capacities = [[row[0], row[4]] for row in self._capacityCalculations]

        return np.array(capacities)
