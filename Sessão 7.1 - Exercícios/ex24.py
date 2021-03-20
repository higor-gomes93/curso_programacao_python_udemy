'''
Faça um programa que leia 10 conjuntos de valores, o primeiro representando o número do aluno e o segundo representando
a sua altura em metros. Encontre o aluno mais baixo e o mais alto. Mostre o número do aluno mais baixo e do mais alto,
juntamente com suas alturas.
'''

dicionario = {}

while len(dicionario) < 10:
    chave = int(input(f'Digite o número do {len(dicionario)+1}º aluno: '))
    valor = float(input(f'Digite a altura do {len(dicionario)+1}º aluno: '))
    dicionario[chave] = valor

for i in dicionario:
    if dicionario[i] == max(dicionario.values()):
        print(f"O aluno mais alto tem {max(dicionario.values())}m e seu número é {i}.")
    elif dicionario[i] == min(dicionario.values()):
        print(f"O aluno mais baixo tem {min(dicionario.values())}m e seu número é {i}.")
