'''
Crie uma classe Agenda que pode armazenar 10 pessoas e seja capaz de realizar as seguintes operações:
- armazena_pessoa(nome, idade, altura);
- remove_pessoa(nome);
- busca_pessoa(nome); // informa em que posição da agenda está a pessoa
- imprime_agenda(); // imprime os dados de todas as pessoas da agenda
- imprime_pessoa(index); // imprime os dados da pessoa que está na posição "i" da agenda
'''

class Agenda:

    agenda_geral = []

    @classmethod
    def imprime_pessoa(cls, index):
        print(cls.agenda_geral[index-1])
        return

    @staticmethod
    def imprime_agenda():
        print(Agenda.agenda_geral)
        return

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def armazena_pessoa(self):
        dado = (self.__nome, self.__idade, self.__altura)
        Agenda.agenda_geral.append(dado)
        return
    
    def remove_pessoa(self):
        for dado in Agenda.agenda_geral:
            if dado[0] == self.__nome:
                Agenda.agenda_geral.remove(dado)
        return

    def busca_pessoa(self):
        for dado in Agenda.agenda_geral:
            if dado[0] == self.__nome:
                posicao = Agenda.agenda_geral.index(dado)
        print(f'{self.__nome} está na posição {posicao+1} da agenda.')
        return
        

pessoa1 = Agenda('Higor', 26, 1.81)
pessoa2 = Agenda('Camila', 23, 1.56)

pessoa1.armazena_pessoa()
pessoa2.armazena_pessoa()

pessoa1.remove_pessoa()

pessoa1.armazena_pessoa()

pessoa1.busca_pessoa()

Agenda.imprime_agenda()

Agenda.imprime_pessoa(1)
