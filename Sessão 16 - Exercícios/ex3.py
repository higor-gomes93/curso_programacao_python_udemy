'''
Crie uma classe denominada Elevador para armazenar as informações de um elevador dentro de um prédio.
A classe deve armazenar o andar atual (térreo = 0), total de andares no prédio, excluindo o térreo,
capacidade do elevador, e quantas pessoas estão presentes nele.

A classe deve também disponibilizar os seguintes métodos:

- Inicializa: que deve receber como parâmetros a capacidade do elevador e o total de andares no prédio
(os elevadores sempre começam no térreo e vazio);
- Entra: para acrescentar uma pessoa no elevador (só deve acrescentar se ainda houver espaço);
- Sai: para remover uma pessoa do elevador (só deve remover se houver alguém dentro dele);
- Sobe: para subir um andar (não deve subir se já estiver no último andar);
- Desce: para descer um andar (não deve descer se já estiver no térreo);
- Encapsular todos os atributos de classe (criar os métodos set e get).
'''

class Elevador:

    def __init__(self, capacidade, totalandares, andar=0, lotacao=0):
        self.__capacidade = capacidade
        self.__totalandares = totalandares
        self.__andar = andar
        self.__lotacao = lotacao

    def entra(self):
        if self.__lotacao < self.__capacidade:
            self.__lotacao += 1
            print(f'Uma pessoa acabou de entrar no elevador. Lotação atual: {self.__lotacao}.')
        else:
            print(f'Capacidade máxima de {self.__capacidade} pessoas já foi atingida.')
        return
    
    def sai(self):
        if self.__lotacao > 0:
            self.__lotacao -= 1
            print(f'Uma pessoa acabou de sair do elevador. Locação atual: {self.__lotacao}.')
        else:
            print(f'Não tem ninguém no elevador. Capacidade total: {self.__capacidade}.')

    def sobe(self):
        if self.__andar < self.__totalandares:
            self.__andar += 1
            print(f'O elevador agora está no andar {self.__andar}.')
        else:
            print(f'O elevador já está no último andar. Total de andares: {self.__totalandares}.')
        return
    
    def desce(self):
        if self.__andar > 0:
            self.__andar -= 1
            print(f'O elevador agora está no andar {self.__andar}.')
        else:
            print(f'O elevador já está no térreo. Total de andares: {self.__totalandares}.')
        return
    

elevador = Elevador(5, 20)
elevador.sobe()
elevador.entra()
elevador.desce()