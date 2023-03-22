import csv

class Functions:

    def __init__(self):
        self.__dicctionary = {}

    def read_data(self):
        cont = 1
        
        etiquetas = ["type", "fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "PH", "sulphates", "alcochol"]

        with open('winequality.csv', 'r') as file:
            reader = csv.reader(file)

            for row in reader:
                #print(row)
                dato = f"dato{str(cont)}"
                #self.__dicctionary = {dato}
                
                for item in row:
                    cont2 = 0
                    self.__dicctionary.append({dato: {etiquetas[cont2]: item}})
                    cont2 += 1

                cont += 1
                print(self.__dicctionary)

                

            



f = Functions()

f.read_data()