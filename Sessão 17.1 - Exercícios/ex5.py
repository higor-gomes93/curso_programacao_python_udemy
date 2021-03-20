'''
Escreva um código que represente a classe Retângulo, com atributos comprimento, largura, área e 
perímetro, e os métodos calcular_area, calcular_perimetro e imprimir. Os métodos calcular_area e 
calcular_perimetro devem  efetuar seus respectivos cálculos e colocar os valores nos atributos área 
e perímetro. O método imprimir deve mostrar na tela os valores de todos os atributos.
'''

class Retangulo:

    def __init__(self, comprimento, largura, area=None, perimetro=None):
        self.__comprimento = comprimento
        self.__largura = largura
        self.__area = area
        self.__perimetro = perimetro

    def calcular_area(self):
        area = self.__comprimento*self.__largura
        self.__area = area
        return

    def calcular_perimetro(self):
        perimetro = self.__comprimento*2 + self.__largura*2
        self.__perimetro = perimetro
        return
    
    def imprimir(self):
        print(f'Comprimento: {self.__comprimento}')
        print(f'Largura: {self.__largura}')
        print(f'Área: {self.__area}')
        print(f'Perímetro: {self.__perimetro}')


retangulo1 = Retangulo(4, 5)
retangulo1.imprimir()
retangulo1.calcular_area()
retangulo1.calcular_perimetro()
retangulo1.imprimir()
