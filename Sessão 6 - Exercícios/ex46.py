'''
Faça um programa que gere um número aleatório de 1 a 1000. O usuário deve tentar acertar qual o
número foi gerado, e a cada tentativa o programa deverá informar se o chute é menor ou maior que
o número gerado. O programa acaba quando o usuário acerta o número gerado. O programa deve informar
em quantas tentativas o número foi descoberto.
'''

import random as r

total = 1000
var = r.randrange(1, total)

num = int(input("Qual número estou pensando? "))
cont = 0

if num == var:
    print("Parabéns! Você acertou de primeira!")

while True:
    if num > var:
        print("Você chutou um valor maior.\n")
        cont = cont + 1
    elif num < var:
        print("Você chutou um valor menor.\n")
        cont = cont + 1
    elif num == var:
        cont = cont + 1
        print(f"Parabéns, você acertou depois de {cont} tentativas.")
        break
    num = int(input("Insira um novo número: "))
