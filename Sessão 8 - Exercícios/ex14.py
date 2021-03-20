'''
Faça uma função que receba a distância em km e a quantidade de litros de gasolina consumidos por um carro em um
percurso, calcule o consumo em km/l e escreva uma mensagem de acordo com a tabela abaixo:

Consumo       Km/l        Mensagem
menor que      8       Venda o carro!
entre        8 e 12      Econômico!
maior que      12      Super econômico
'''

def gasto_carro(distancia, litros):
    consumo = distancia/litros
    if consumo < 8:
        return 'Venda o carro!'
    elif 8 <= consumo <= 12:
        return 'Econômico!'
    elif consumo > 12:
        return 'Super econômico!'
    return 'Valor inválido'

print(gasto_carro(14, 3))
print(gasto_carro(24, 3))
print(gasto_carro(34, 3))
print(gasto_carro(44, 3))
