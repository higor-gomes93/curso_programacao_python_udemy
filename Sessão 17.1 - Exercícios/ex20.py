'''
Escreva um código que apresente a classe Televisor, com as seguintes características:
1. Atributos:
- ligado
- canal
- volume
- numerocanais
- volumemaximo
2. Métodos:
- imprimir
- ligar e desligar
- canal_acima e canal_abaixo (chegou ao mínimo, vai pro máximo, e vice versa)
- volume_acima e volume_abaixo (chegou ao máximo, não vai mais, o mesmo com o mínimo)
'''

class Televisor:

    def __init__(self, numerocanais, volumemaximo, ligado=False, canal=1, volume=1):
        self.__numerocanais = numerocanais
        self.__volumemaximo = volumemaximo
        self.__ligado = ligado
        self.__canal = canal
        self.__volume = volume
    
    def power(self):
        if self.__ligado == False:
            self.__ligado = True
            print('Televisor ligou')
        else:
            self.__ligado = False
            print('Televisor desligou')
    
    def canal_acima(self):
        if self.__canal < self.__numerocanais:
            self.__canal += 1
        elif self.__canal == self.__numerocanais:
            self.__canal = 1
        print(f'Canal: {self.__canal}')

    def canal_abaixo(self):
        if self.__canal > 1:
            self.__canal -= 1
        elif self.__canal == 1:
            self.__canal = self.__numerocanais
        print(f'Canal: {self.__canal}')

    def volume_acima(self):
        if self.__volume < self.__volumemaximo:
            self.__volume += 1
            print(f'Volume: {self.__volume}')
        elif self.__volume == self.__volumemaximo:
            print(f'Volume máximo: {self.__volume}')

    def volume_abaixo(self):
        if self.__volume > 1:
            self.__volume -= 1
            print(f'Volume: {self.__volume}')
        elif self.__volume == 1:
            print(f'Volume mínimo: {self.__volume}')

    def imprimir(self):
        if self.__ligado == True:
            print('Status: ligado')
        elif self.__ligado == False:
            print('Status: desligado')
        print(f'Total de canais: {self.__numerocanais}')
        print(f'Volume máximo: {self.__volumemaximo}')
        print(f'Canal atual: {self.__canal}')
        print(f'Volume atual: {self.__volume}')
        
televisao1 = Televisor(10, 10)

while True:
    print('Digite o que deseja fazer')
    print('I - Imprimir o status do televisor')
    print('V+ - Subir o volume')
    print('V- - Abaixar o volume')
    print('C+ - Subir o canal')
    print('C- - Abaixar o canal')
    print('P - Ligar ou desligar')
    print('X - Sair')
    acao = input('-> ')
    print()
    if acao == 'X':
        break
    elif acao == 'I':
        televisao1.imprimir()
    elif acao == 'V+':
        televisao1.volume_acima()
    elif acao == 'V-':
        televisao1.volume_abaixo()
    elif acao == 'C+':
        televisao1.canal_acima()
    elif acao == 'C-':
        televisao1.canal_abaixo()
    elif acao == 'P':
        televisao1.power()
    print()
