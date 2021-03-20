'''
Faça uma função que receba a data atual (dia, mês e ano em inteiro) e exiba-a na tela no formato textual
por extenso.
'''

# Primeira maneira
def data_converter(data):
    dicionario = {'01': 'Janeiro', '02': 'Fevereiro', '03': 'Março', '04': 'Abril', '05': 'Maio', '06': 'Junho', 
    '07': 'Julho', '08': 'Agosto', '09': 'Setembro', '10': 'Outubro', '11': 'Novembro', '12': 'Dezembro'}
    array = data.split('/')
    mes = dicionario[array[1]]
    extenso = f"{array[0]} de {mes} de {array[2]}"
    return extenso

print()
print(data_converter('01/02/2020'))

# Segunda maneira
def data_converter(data):
    dicionario = {'01': 'Janeiro', '02': 'Fevereiro', '03': 'Março', '04': 'Abril', '05': 'Maio', '06': 'Junho', 
    '07': 'Julho', '08': 'Agosto', '09': 'Setembro', '10': 'Outubro', '11': 'Novembro', '12': 'Dezembro'}
    array = data.split('/')
    mes = dicionario[array[1]]
    extenso = f"{array[0]} de {mes} de {array[2]}"
    print(extenso)
    return 

print()
data_converter('01/02/2020')