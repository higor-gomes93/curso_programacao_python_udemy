'''
Escreva um código que apresente a classe Circulo, com atributos raio, área e perímetro, e os métodos
calcular_area, calcular_perimetro e imprimir. Os métodos calcular_area e calcular_perimetro devem 
efetuar seus respectivos cálculos e colocar os valores nos atributos área e perímetro. O método 
imprimir deve mostrar na tela os valores de todos os atributos.
'''

from math import pi

class Circulo:

    def __init__(self, raio, area=None, perimetro=None):
        self.__raio = raio
        self.__area = area
        self.__perimetro = perimetro

    def calcular_area(self):
        area = pi*(self.__raio**2)
        self.__area = area
        return  

    def calcular_perimetro(self):
        perimetro = 2*pi*self.__raio
        self.__perimetro = perimetro
        return

    def imprimir(self):
        print(f'Raio: {self.__raio}\nÁrea: {self.__area}\nPerímetro: {self.__perimetro}')
        return

quadrado1 = Circulo(2)
quadrado2 = Circulo(4)

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
