class Equipamento:

    def __init__(self, voltagem, material):
        self.__voltagem = voltagem
        self.__material = material
    
    @property
    def voltagem(self):
        return self.__voltagem
    
    @property
    def material(self):
        return self.__material
    
    @voltagem.setter
    def voltagem(self, valor):
        self.__voltagem = valor
        return
    
    @material.setter
    def material(self, valor):
        self.__material = valor
        return

    def exibir(self):
        print(self.__voltagem)
        print(self.__material)


class Computador(Equipamento):

    def __init__(self, voltagem, material, ram, hd):
        super().__init__(voltagem, material)
        self.__ram = ram
        self.__hd = hd
    
    @property
    def ram(self):
        return self.__ram
    
    @property
    def hd(self):
        return self.__hd
    
    @ram.setter
    def ram(self, valor):
        self.__ram = valor
        return
    
    @hd.setter
    def hd(self, valor):
        self.__hd = valor
        return

    def exibir(self):
        super().exibir()
        print(self.__ram)
        print(self.__hd)
        return


class TreinaEquipamento:

    equipamento1 = Equipamento(110, 'Alumínio')
    computador1 = Computador(220, 'Acrílico', '12GB', '1TB')

    @classmethod
    def main(cls):
        print(cls.equipamento1.voltagem)
        print(cls.equipamento1.material)
        print(cls.computador1.voltagem)
        print(cls.computador1.material)
        print(cls.computador1.ram)
        print(cls.computador1.hd)
        return


TreinaEquipamento.main()
print()
equipamento1 = Equipamento(110, 'Alumínio')
computador1 = Computador(220, 'Acrílico', '12GB', '1TB')
equipamento1.exibir()
print()
computador1.exibir()
