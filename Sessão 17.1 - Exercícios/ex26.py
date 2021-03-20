'''
Escreva um código que apresente a classe Microondas com as seguintes características:
1. Atributos
- ligado
- portafechada
2. Métodos
- ligar e desligar (apenas com a porta fechada)
- fechar_porta e abir_porta
- imprimir
'''

class Microondas:

    def __init__(self, ligado=False, portafechada=True):
        self.__ligado = ligado
        self.__portafechada = portafechada
    
    def power(self):
        if self.__portafechada == True and self.__ligado == False:
            self.__ligado = True
            print('Microondas ligado')
        elif self.__ligado == True:
            self.__ligado = False
            print('Microondas desligado')
        elif self.__portafechada == False:
            print('Porta aberta - Impossível ligar')
    
    def porta(self):
        if self.__ligado == False and self.__portafechada == True:
            self.__portafechada = False
            print('Porta aberta')
        elif self.__portafechada == False:
            self.__portafechada = True
            print('Porta fechada')
        elif self.__ligado == True:
            print('Microondas ligado - Impossível abrir a porta')
    
    def imprimir(self):
        if self.__ligado == True:
            print('Microondas ligado')
        elif self.__ligado == False:
            print('Microondas desligado')
        
        if self.__portafechada == True:
            print('Porta fechada')
        elif self.__portafechada == False:
            print('Porta aberta')

micro1 = Microondas()

while True:
    print('Digite o que deseja fazer')
    print('I - Imprimir o status do microondas')
    print('A - Abrir ou fechar a porta')
    print('P - Ligar ou desligar')
    print('X - Sair')
    acao = input('-> ')
    print()
    if acao == 'X':
        break
    elif acao == 'I':
        micro1.imprimir()
    elif acao == 'A':
        micro1.porta()
    elif acao == 'P':
        micro1.power()
    print()
