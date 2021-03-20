'''
Escreva um programa que receba como entrada o valor do saque realizado pelo cliente de um banco
e retorne quantas notas de cada valor serão necessárias para atender ao saque com a menor quantidade
de notas possível. Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 real.
'''

valor = int(input("Quanto você deseja sacar? "))
cont_100 = 0
cont_50 = 0
cont_20 = 0
cont_10 = 0
cont_5 = 0
cont_2 = 0
cont_1 = 0

while valor > 0:
    if valor >= 100:
        valor -= 100
        cont_100 += 1
    elif 50 <= valor < 100:
        valor -= 50
        cont_50 += 1
    elif 20 <= valor < 50:
        valor -= 20
        cont_20 += 1
    elif 10 <= valor < 20:
        valor -= 10
        cont_10 += 1
    elif 5 <= valor < 10:
        valor -= 5
        cont_5 += 1
    elif 2 <= valor < 5:
        valor -= 2
        cont_2 += 1
    elif valor < 2:
        valor -= 1
        cont_1 += 1

print("Serão emitidas:")
if cont_100 != 0:
    print(f"{cont_100} nota(s) de 100")
if cont_50 != 0:
    print(f"{cont_50} nota(s) de 50")
if cont_20 != 0:
    print(f"{cont_20} nota(s) de 20")
if cont_10 != 0:
    print(f"{cont_10} nota(s) de 10")
if cont_5 != 0:
    print(f"{cont_5} nota(s) de 5")
if cont_2 != 0:
    print(f"{cont_2} nota(s) de 2")
if cont_1 != 0:
    print(f"{cont_1} nota(s) de 1")
