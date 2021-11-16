import csv
from os import times
import matplotlib.pyplot as plt
import numpy as np
from Calculators.CapacityCalculator import CapacityCalculator
from Calculators.TemperatureCalculator import TemperatureCalculator 
from Settings import Settings

settings = Settings()


#############################################
# Cooling of resistor
#############################################

cooling_block = TemperatureCalculator(settings)
cooling_block.LoadMeasurements("Lab1\cooling_resistor.csv")
cooling_block.CalculateMeanVoltages()
cooling_block.CalculateTemperatures()

temps = cooling_block.GetTemperatures()
plot = plt.plot(temps[:,0], temps[:,1])

# Show means line
means = np.empty(len(temps), dtype=float)
means.fill(cooling_block.MeanTemperatureSlope()*30)
plt.plot(temps[:,0], means, "r--")
plt.annotate(str(round(means[2],4)), xy=(700,means[2]))

plt.grid(True)
plt.title("Cooling resistor")
plt.xlabel("Time")
plt.ylabel("Temperature difference for interval")
plt.legend(["Measurements", "Mean value"])

plt.show()

#############################################
# Heating of resistor
# Calculate specific heat capacity to be 
# withdrawn from full experiment
#############################################

heating_resistor = CapacityCalculator(settings)
heating_resistor.LoadMeasurements("Lab1\heating_resistor.csv")
heating_resistor.CalculateMeanVoltages()
heating_resistor.CalculateTemperatures()
heating_resistor.CalculateCapacity(settings.current2, settings.reistorMass, 0, cooling_block.MeanTemperatureSlope())
resistor_heat_capacify_mean = heating_resistor.MeanHeatCapacity()
print("resistor_heat_capacify_mean= ", resistor_heat_capacify_mean)


#############################################
# Cooling of full experiment, block+resistor
#############################################

cooling_full = TemperatureCalculator(settings)
cooling_full.LoadMeasurements("Lab1\cooling_full.csv")
cooling_full.CalculateMeanVoltages()
cooling_full.CalculateTemperatures()

temps = cooling_full.GetTemperatures()
plot = plt.plot(temps[:,0], temps[:,1])

# Show means line
means = np.empty(len(temps), dtype=float)
means.fill(cooling_full.MeanTemperatureSlope()*30)
plt.plot(temps[:,0], means, "r--")
plt.annotate(str(round(means[2],4)), xy=(700,means[2]))

plt.grid(True)
plt.title("Cooling block+resistor")
plt.xlabel("Time")
plt.ylabel("Temperature difference for interval")
plt.legend(["Measurements", "Mean value"])

plt.show()


#############################################
# Heating of full experiment, block+resistor
#############################################


heating_full = CapacityCalculator(settings)
heating_full.LoadMeasurements("Lab1\heating_full.csv")
heating_full.CalculateMeanVoltages()
heating_full.CalculateTemperatures()
heating_full.CalculateCapacity(settings.current1, settings.blockMass, resistor_heat_capacify_mean, cooling_full.MeanTemperatureSlope())

capacities = heating_full.GetSpecificHeats()
plot = plt.plot(capacities[:,0], capacities[:,1], color='blue', marker='o')


z = np.polyfit(capacities[:,0], capacities[:,1], 3)
p = np.poly1d(z)
plt.plot(capacities[:,0],p(capacities[:,0]),"g-")

means = np.empty(len(capacities), dtype=float)
means.fill(heating_full.MeanSpecificHeat())
plt.plot(capacities[:,0], means, "r--")
plt.annotate(str(round(means[2],1)), xy=(300,means[2]))

plt.grid(True)
plt.title("Heating block+resistor")
plt.xlabel("Time")
plt.ylabel("Specific heat")
plt.legend(["Measurements", "Matching curve", "Mean value"])

for i,j in zip(capacities[:,0], capacities[:,1]):
    plt.annotate(str(round(j,1)), xy=(i-10,j+3))


plt.show()

