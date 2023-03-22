import csv

class Functions:

    def __init__(self):
        self.__dicctionary = {}

    def read_data(self):
        cont = 1
        
        etiquetas = ["type", "fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", ]

        with open('winequality.csv', 'r') as file:
            reader = csv.reader(file)

            for row in reader:
                #print(row)
                dato = f"dato{str(cont)}"
                self.__dicctionary = {dato}
                cont += 1
                for item in row:
                    self.__dicctionary[dato]

                

            



f = Functions()

f.read_data()