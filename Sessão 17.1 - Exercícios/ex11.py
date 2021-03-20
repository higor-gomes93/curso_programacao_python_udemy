'''
Baseando-se na classe Moto, adicione os métodos marcha_acima e marcha_abaixo, que sobem ou abaixam
a marcha em uma unidade, os atributos marchamenor e marchamaior (que limitam os métodos de mudança 
de marcha), o atributo ligada (boolean) que indica se a moto está ligada ou não, e os métodos ligar
e desligar.
'''

class Moto:

    def __init__(self, marca, modelo, cor, marchamaior, marcha=0, marchamenor=0, ligada=False):
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__marcha = marcha
        self.__marchamaior = marchamaior
        self.__marchamenor = marchamenor
        self.__ligada = ligada
    
    def marcha_acima(self):
        if self.__marcha < self.__marchamaior:
            self.__marcha += 1
        else:
            print('Já está na última marcha')

    def marcha_abaixo(self):
        if self.__marcha > self.__marchamenor:
            self.__marcha -= 1
        else:
            print('Já está na primeira marcha')

    def ligar(self):
        if self.__ligada == False:
            self.__ligada = True
        else:
            print('A moto já está ligada')

    def desligar(self):
        if self.__ligada == True:
            self.__ligada = False
        else:
            print('A moto já está desligada')

    def imprimir(self):
        print(f'Marca: {self.__marca}')
        print(f'Modelo: {self.__modelo}')
        print(f'Cor: {self.__cor}')
        print(f'Marchas: {self.__marchamaior}')
        print(f'Marcha atual: {self.__marcha}')
        if self.__ligada == True:
            print('Ligada')
        else:
            print('Desligada')
        return
    

motinho = Moto('Honda Bis', 'XS-320', 'Vermelha', 3)

while True:
    print('Digite o que deseja fazer')
    print('I - Imprimir o status da moto')
    print('S - Subir a marcha')
    print('A - Abaixar a marcha')
    print('L - Ligar a moto')
    print('D - Desligar a moto')
    print('X - Sair')
    acao = input('-> ')
    print()
    if acao.upper() == 'X':
        break
    elif acao.upper() == 'I':
        motinho.imprimir()
    elif acao.upper() == 'S':
        motinho.marcha_acima()
    elif acao.upper() == 'A':
        motinho.marcha_abaixo()
    elif acao.upper() == 'L':
        motinho.ligar()
    elif acao.upper() == 'D':
        motinho.desligar()
    print()
