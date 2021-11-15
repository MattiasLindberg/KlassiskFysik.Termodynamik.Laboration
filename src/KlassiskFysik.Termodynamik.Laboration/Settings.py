import csv


class Settings:

    def __init__(self):
        # read csv file as a list of lists
        with open('experiment_settings.csv', 'r') as read_obj:
            csv_reader = csv.reader(read_obj, delimiter = '	', quoting = csv.QUOTE_NONNUMERIC)
            settings = list(csv_reader)
            print(settings)

        self.current = settings[1][3]
        self.impedance = settings[1][2]
        self.blockMass = settings[1][0]
