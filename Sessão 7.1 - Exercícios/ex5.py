'''
Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui.
'''

lista = []
cont = 0

while len(lista) < 10:
    num = int(input("Digite um número: "))
    lista.append(num)

for i in lista:
    if i%2 == 0:
        cont += 1

if cont == 1:
    print(f"Na lista existe {cont} número par.")
elif cont > 1:
    print(f"Na lista existem {cont} números pares.")
