import csv
import numpy as np
from TemperatureCalculator import TemperatureCalculator

class CapacityCalculator(TemperatureCalculator):

    def __init__(self, settings):
        super(CapacityCalculator, self).__init__(settings)

    def CalculateCapacity(self):
        self._capacityCalculations = list()
        self.CalculateTemperatures()

        for temp in self._temperatures:
            time = temp[0];
            timeInterval = temp[1];
            temperatureDiff = temp[2];

            heat = self.settings.current * self.settings.current * self.settings.impedance * timeInterval

            C = heat / temperatureDiff
            adjustedC = C - 33.03
            cp = adjustedC / self.settings.blockMass

            self._capacityCalculations.append([time, timeInterval, temperatureDiff, heat, C, adjustedC, cp])

    def MeanCapacity(self):
        return np.mean(self.GetCapacities()[:,1])

    def GetCapacities(self):
        capacities = [[row[0], row[6]] for row in self._capacityCalculations]

        return np.array(capacities)
