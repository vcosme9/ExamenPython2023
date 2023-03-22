import csv

class Functions:

    #def __init__(self):
        #self.__file = file

    def read_data(self):
        with open('winequality.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

            [None] + [{} for row in reader]



f = Functions()

f.read_data()