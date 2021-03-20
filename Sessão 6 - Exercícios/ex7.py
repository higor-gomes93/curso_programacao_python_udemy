'''
Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média.
'''
i = 1
soma = 0
while i <= 10:
    cont = int(input(f"Insira o numero {i}: "))
    if cont > 0:
        i += 1
        num = cont
        soma = soma + num
    else:
        print("Numero invalido. Insira um numero positivo.")
    total = i-1
media = soma/total
print(f"A media dos numeros eh {media}")