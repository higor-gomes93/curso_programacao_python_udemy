'''
Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.
'''
valor = float(input("Digite o numero 1: "))
maximo = valor
minimo = valor

for i in range(2, 11):
    num = float(input(f"Digite o numero {i}: "))
    if num >= maximo:
        maximo = num
    elif num <= minimo:
        minimo = num
    
print(f"O valor maximo eh {maximo} e o valor minimo eh {minimo}")

   