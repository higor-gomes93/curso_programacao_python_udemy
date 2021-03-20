'''
Escreva um código que apresente a classe Eletrodoméstico, com atributo ligado e o método imprimir.
O método imprimir deve mostrar na tela os valores de todos os atributos. O atributo ligado será
boleano e deverá indicar o estado atual do eletrodoméstico, se ligado ou desligado.
'''

class Eletrodomestico:

    def __init__(self, ligado=False):
        self.__ligado = ligado
    
    def ligar(self):
        if self.__ligado == False:
            self.__ligado = True
        else:
            print('O eletrodoméstico já está ligado')

    def desligar(self):
        if self.__ligado == True:
            self.__ligado = False
        else:
            print('O eletrodoméstico já está desligado')

    def imprimir(self):
        if self.__ligado == True:
            print(f'Status do eletrodoméstico: ligado')
        else:
            print(f'Status do eletrodoméstico: desligado')


microondas = Eletrodomestico()

microondas.imprimir()
microondas.ligar()
microondas.imprimir()
microondas.ligar()
microondas.desligar()
microondas.imprimir()
microondas.desligar()