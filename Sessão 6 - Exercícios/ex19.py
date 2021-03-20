'''
Escreva um algoritmo quqe leia um número inteiro entre 100 e 999 e imprima na saída cada um dos
algarismos que compõe o número.
'''
# Primeira maneira
teste = input("Insira um numero inteiro de 3 dígitos: ")
print(f"Primeiro algarismo: {teste[0]}")
print(f"Segundo algarismo: {teste[1]}")
print(f"Terceiro algarismo: {teste[2]}")

# Segunda maneira
num = int(input("Insira um numero inteiro de 3 dígitos: "))

if 100 <= num <= 999:
    num = str(num)
    for _,alg in enumerate(num):
        print(alg[0], end = ' ')
