'''
Crie um programa que lê 6 valores inteiros pares e, em seguida, mostre na tela os valores lidos 
na ordem inversa.
'''

lista = []

while len(lista) < 6:
    num = int(input("Digite um número inteiro: "))
    if num%2 == 0:
        lista.append(num)

print(lista)
lista.reverse()
print(lista)
