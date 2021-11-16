import csv
import numpy as np

class Calculator:

    def __init__(self, settings):
        self.settings = settings

    def LoadMeasurements(self, filename):
        with open(filename, 'r') as read_obj:
            csv_reader = csv.reader(read_obj, delimiter = '	', quoting = csv.QUOTE_NONNUMERIC)
            self.measurements = list(csv_reader)
