'''
Elabore um programa que faça a leitura de vários números inteiros, até que se digite um número
negativo. O programa tem que retornar o maior e o menor número lido.
'''
num = int(input("Digite um número inteiro: "))

if num < 0:
    print("Número inválido.")
    num = int(input("Digite um número inteiro: "))
else:
    maximo = num
    minimo = num

while num >= 0:
    num = int(input("Digite um número inteiro: "))
    if num >= 0:
        if num >= maximo:
            maximo = num
        elif num <= minimo:
            minimo = num

print(f"O valor máximo é {maximo} e o valor mínimo é {minimo}.")
