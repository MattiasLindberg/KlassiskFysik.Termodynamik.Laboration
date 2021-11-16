import csv
import numpy as np
from Calculators.Calculator import Calculator

class TemperatureCalculator(Calculator):

    def __init__(self, settings):
        super(TemperatureCalculator, self).__init__(settings)

    def CalculateMeanVoltages(self):
        self.measurements[0].append("Mean Voltage")

        for measurement in self.measurements[1:len(self.measurements)]:
            meanVoltage = (measurement[1] + measurement[2])/2
            measurement.append(meanVoltage)

    def CalculateTemperatures(self):
        self._temperatures = list()

        loop = 1 # Ignore header row
        while loop < len(self.measurements)-2: # -2 because we merge two rows, last row cannot be merged with another
            measurement1 = self.measurements[loop];
            measurement2 = self.measurements[loop+1];
            #print(measurement1)
            #print(measurement2)
    
            timeInterval = measurement2[0] - measurement1[0]
            voltageDiff = measurement2[3] - measurement1[3]
            temperatureDiff = voltageDiff * 25.08355

            #print(timeInterval)
            #print(voltageDiff)
            #print(temperatureDiff)

            self._temperatures.append([measurement2[0], timeInterval, temperatureDiff, temperatureDiff/timeInterval])

            loop += 1

    def GetTemperatures(self):
        temps2 = [[row[0], row[2]] for row in self._temperatures]
        #print ("Temps= ", temps2)
        return np.array(temps2)
    
    def GetTemperaturSlope(self):
        temps2 = [[row[0], row[3]] for row in self._temperatures]
        #print ("Temps= ", temps2)
        return np.array(temps2)

    def MeanTemperatureSlope(self):
        return np.mean(self.GetTemperaturSlope()[:,1])
