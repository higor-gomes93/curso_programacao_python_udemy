class Pessoa:

    def __init__(self, codigo, nome, idade):
        self.__codigo = codigo
        self.__nome = nome
        self.__idade = idade
        print('Contrutor padrão.')
    
    def exibe(self, parametro=1):
        print(f'Código: {self.__codigo}')
        print(f'Nome: {self.__nome}')
        if parametro == 1:
            print(f'Idade: {self.__idade}')
        return


class TestaPessoa(Pessoa):

    def __init__(self, codigo, nome, idade):
        super().__init__(codigo, nome, idade)
    
    def exibe(self, parametro=1):
        return super().exibe(parametro=parametro)

    
pessoa = TestaPessoa(1234, 'Higor', 26)
pessoa.exibe(2)
pessoa.exibe(1)
pessoa.exibe()
