'''
Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos.
'''

lista = []

while len(lista) < 6:
    valor = int(input("Digite um número inteiro: "))
    lista.append(valor)

print(lista)
