'''
Escreva um código que apresente a classe Pessoa, com atributos nome, endereço e telefone, e o método
imprimir. O método imprimir deve mostrar na tela os valores de todos os atributos.
'''

class Pessoa:

    def __init__(self, nome, endereco, telefone):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone

    def imprimir(self):
        print(f'Nome: {self.__nome}\nEndereço: {self.__endereco}\nTelefone: {self.__telefone}')
        


pessoa1 = Pessoa('Higor Gomes', 'Rua Número 1', '997033467')
pessoa1.imprimir()
