import csv

class Functions:

    def __init__(self):
        self.__dicctionary = {}

    def read_data(self):
        
        etiquetas = ["type", "fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "PH", "sulphates", "alcochol", "quality"]

        with open('winequality.csv', 'r') as file:
            reader = csv.reader(file)
            cont = 1

            self.__dicctionary = [{f"dato": row}  for row in reader]

            '''No he conseguido sacar el diccionario como se pedia pero ya he perdido mucho tiempo en esto

            Tiene el siguiente formato:

            {
                'dato': [red, ....],
                'dato': [white, ....],
                ....
            
            }
            '''    
            #print(self.__dicctionary)

    def split(self):
        list_white = []
        list_red = []
        for key in self.__dicctionary:
            if self.__dicctionary[key][0] == 'white':
                list_white.append(self.__dicctionary[key])
            elif self.__dicctionary[key][0] == 'red':
                list_red.append(self.__dicctionary[key])

        print(list_white)





                

            



f = Functions()

f.read_data()
f.split()