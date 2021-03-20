'''
Escreva um programa que leia 10 números inteiros e os armazene em um vetor. Imprima o vetor, o maior
elemento e a posição que ele se encontra.
'''

lista = []

while len(lista) < 10:
    num = int(input("Digite um número inteiro: "))
    lista.append(num)

print(lista)
maximo = max(lista)
print(f"O valor máximo é {maximo}.")
print(f"A posição do valor máximo é {lista.index(maximo)}.")
