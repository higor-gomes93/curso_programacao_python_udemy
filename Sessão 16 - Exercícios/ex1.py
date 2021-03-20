'''
Crie uma classe para representar uma pessoa, com os atributos privados de nome, idade e altura. Crie os
métodos públicos necessários para sets e gets e também um método para imprimir os dados de uma pessoa.
'''

class Pessoa:

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        self.__nome = valor
        return self.__nome
    
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, valor):
        self.__idade = valor
        return self.__idade

    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self, valor):
        self.__altura = valor
        return self.__altura
    
    def imprime_dados(self):
        return f'Nome: {self.__nome} - Idade: {self.__idade} - Altura: {self.__altura}'
    
pessoa1 = Pessoa('Higor', 26, 1.81)
pessoa2 = Pessoa('Camila', 23, 1.65)

print(pessoa1.imprime_dados())
print(pessoa2.nome)
pessoa1.nome = 'Higor Gomes'
print(pessoa1.nome)
