import csv

class Functions:

    def __init__(self):
        self.__dicctionary = {}

    def read_data(self):
        cont = 1
        
        etiquetas = ["type", "fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "PH", "sulphates", "alcochol"]

        with open('winequality.csv', 'r') as file:
            reader = csv.reader(file)

            self.__dicctionary = [{etiqueta:None for etiqueta in etiquetas} for row in reader]
                
            
                   
            print(self.__dicctionary)

                

            



f = Functions()

f.read_data()