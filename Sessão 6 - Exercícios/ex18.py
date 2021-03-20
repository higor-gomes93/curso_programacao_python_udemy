'''
Escreva um algoritmo que leia uma certa quantidade de números e imprima o maior deles e quantas vezes
o maior número foi lido. A quantidade de números a serem lidos deve ser fornecida pelo usuário.
'''

qtd = int(input("Quantos numeros serao lidos? "))
cont = 1

if qtd == 1:
    num = int(input("Digite o numero 1: "))
    print(f"O maior deles eh o numero {num} e ele foi contado 1 vez.")
else:
    valor = int(input("Digite o numero 1: "))
    maximo = valor
    for i in range(2, qtd+1, 1):
        num = int(input(f"Digite o numero {i}: "))
        if num > maximo:
            maximo = num
        elif num == maximo:
            cont = cont + 1

print(f"O maior deles eh o numero {maximo} e ele foi lido {cont} vez(es).")
