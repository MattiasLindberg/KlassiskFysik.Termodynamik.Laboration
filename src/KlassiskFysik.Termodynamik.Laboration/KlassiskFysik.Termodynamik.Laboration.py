
import csv
from os import times
import matplotlib.pyplot as plt
import numpy as np
from CapacityCalculator import CapacityCalculator
from TemperatureCalculator import TemperatureCalculator 
from Settings import Settings

settings = Settings()



cooling = TemperatureCalculator(settings)
cooling.LoadMeasurements("cooling_full.csv")
cooling.CalculateMeanVoltages()
cooling.CalculateTemperatures()

temps = cooling.GetTemperaturDifferences()
plot = plt.plot(temps[:,0], temps[:,1])

means = np.empty(len(temps), dtype=float)
means.fill(cooling.MeanTemperature())
plt.plot(temps[:,0],means,"r--")
plt.annotate(str(round(means[2],4)), xy=(700,means[2]))

plt.show()


heating = CapacityCalculator(settings)
heating.LoadMeasurements("heating_full.csv")
heating.CalculateMeanVoltages()
heating.CalculateTemperatures()
heating.CalculateCapacity()
heating.MeanCapacity()

capacities = heating.GetCapacities()
plot = plt.plot(capacities[:,0], capacities[:,1], color='blue', marker='o')


z = np.polyfit(capacities[:,0], capacities[:,1], 3)
p = np.poly1d(z)
plt.plot(capacities[:,0],p(capacities[:,0]),"g-")

means = np.empty(len(capacities), dtype=float)
means.fill(heating.MeanCapacity())
plt.plot(capacities[:,0],means,"r--")
plt.annotate(str(round(means[2],1)), xy=(300,means[2]))

plt.grid(True)
plt.xlabel("Time")
plt.ylabel("Heat capacity")
plt.legend(["Calculated values", "Matching curve", "Mean value"])

for i,j in zip(capacities[:,0], capacities[:,1]):
    plt.annotate(str(round(j,1)), xy=(i-10,j+3))


plt.show()

