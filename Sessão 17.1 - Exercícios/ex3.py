'''
Escreva um código que apresente a classe Quadrado, com atributos lado, área e perímetro, e os métodos
calcular_area, calcular_perimetro e imprimir. Os métodos calcular_area e calcular_perimetro devem 
efetuar seus respectivos cálculos e colocar os valores nos atributos área e perímetro. O método 
imprimir deve mostrar na tela os valores de todos os atributos.
'''

class Quadrado:

    def __init__(self, lado, area=None, perimetro=None):
        self.__lado = lado
        self.__area = area
        self.__perimetro = perimetro

    def calcular_area(self):
        area = self.__lado*self.__lado
        self.__area = area
        return  

    def calcular_perimetro(self):
        perimetro = self.__lado*4
        self.__perimetro = perimetro
        return

    def imprimir(self):
        print(f'Lado: {self.__lado}\nÁrea: {self.__area}\nPerímetro: {self.__perimetro}')
        return

quadrado1 = Quadrado(2)
quadrado2 = Quadrado(4)

quadrado1.imprimir()
quadrado2.imprimir()

quadrado1.calcular_area()
quadrado2.calcular_area()

quadrado1.imprimir()
quadrado2.imprimir()

quadrado1.calcular_perimetro()
quadrado2.calcular_perimetro()

quadrado1.imprimir()
quadrado2.imprimir()
