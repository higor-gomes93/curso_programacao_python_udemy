'''
Escreva um código que apresente a classe Moto, com atributos marca, modelo, cor e marcha, e o método
imprimir. O método imprimir deve mostrar na tela os valores de todos os atributos. O atributo marcha
indica em que marcha a moto se encontra, sendo representado de forma inteira, onde 0 - neutro, 1 - 
primeira, 2 - segunda, etc.
'''

class Moto:

    def __init__(self, marca, modelo, cor, marcha):
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__marcha = marcha

    def imprimir(self):
        print(f'Marca: {self.__marca}')
        print(f'Modelo: {self.__modelo}')
        print(f'Cor: {self.__cor}')
        print(f'Marcha: {self.__marcha}')
        return


motinho = Moto('Honda Bis', 'XS-320', 'Vermelha', 3)

motinho.imprimir()
