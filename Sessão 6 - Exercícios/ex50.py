'''
Chico tem 1.50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1.10 metro e cresce 3 centímetros
por ano. Escreva um programa que calcule e imprima quantos anos serão necessários para que Zé seja
maior que Chico.
'''

altura_chico = 1.50
altura_ze = 1.10
cont = 0

while altura_ze <= altura_chico:
    altura_chico += 0.02
    altura_ze += 0.03
    cont += 1

print(f"Levará {cont} anos para Zé ser maior que Chico.")
