'''
Crie uma classe Televisão e uma classe ControleRemoto que pode controlar o volume e trocar os canais
da televisão.

- O controle de volume permite aumentar e diminuir a potência do volume de som em uma unidade de
cada vez;
- O controle de canal também permite aumentar e diminuir o número do canal em uma unidade, porém,
também possibilita trocar para um canal indicado;
- Também devem existir métodos para consultar o valor do volume de som e o canal selecionado.
'''

class Televisao:

    def __init__(self):
        self.__canal = 0
        self.__volume = 0

class ControleRemoto:

    def aumentar_volume(self):
        if self._Televisao__volume < 100:
            self._Televisao__volume += 1
            print(f'Volume: {self._Televisao__volume}')
        else:
            print('O volume já está no máximo.')
        return

    def abaixar_volume(self):
        if self._Televisao__volume > 0:
            self._Televisao__volume -= 1
            print(f'Volume: {self._Televisao__volume}')
        else:
            print('O volume já está no mínimo.')

    def aumentar_canal(self):
        if self._Televisao__canal < 50:
            self._Televisao__canal += 1
            print(f'Canal: {self._Televisao__canal}')
        else:
            print('Você já está no último canal.')
        return

    def abaixar_canal(self):
        if self._Televisao__canal > 0:
            self._Televisao__canal -= 1
            print(f'Canal: {self._Televisao__canal}')
        else:
            print('Você já está no primeiro canal.')

    def procurar_canal(self, valor):
        if 0 <= valor <= 50:
            self._Televisao__canal = valor
            print(f'Canal: {self._Televisao__canal}')
        else:
            print(f'Não existe o canal {valor}.')
        
    def volume(self):
        print(f'Volume: {self._Televisao__volume}')
        return
    
    def canal(self):
        print(f'Canal: {self._Televisao__canal}')
        return

tv1 = Televisao()

ControleRemoto.aumentar_volume(tv1)
ControleRemoto.aumentar_volume(tv1)
ControleRemoto.aumentar_volume(tv1)
ControleRemoto.aumentar_volume(tv1)
ControleRemoto.aumentar_volume(tv1)

ControleRemoto.aumentar_canal(tv1)
ControleRemoto.aumentar_canal(tv1)
ControleRemoto.aumentar_canal(tv1)

ControleRemoto.volume(tv1)
ControleRemoto.canal(tv1)

ControleRemoto.procurar_canal(tv1, 45)

ControleRemoto.canal(tv1)
ControleRemoto.aumentar_canal(tv1)
ControleRemoto.aumentar_canal(tv1)
ControleRemoto.aumentar_canal(tv1)
ControleRemoto.aumentar_canal(tv1)
ControleRemoto.aumentar_canal(tv1)
ControleRemoto.aumentar_canal(tv1)
