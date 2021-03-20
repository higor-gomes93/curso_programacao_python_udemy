'''
Faça um programa que leia vários números, calcule e mostre:
(a) A soma dos números digitados
(b) A quantidade de números digitados
(c) A média dos números digitados
(d) O maior número digitado
(e) O menor número digitado
(f) A média dos números pares
'''

soma = 0
cont = 0
cont_pares = 0
soma_pares = 0

while True:
    num = int(input("Digite um número: "))

    if num == 0:
        break

    if cont == 0:
        maximo = num
        minimo = num
    
    if num >= maximo:
        maximo = num
    elif num <= minimo:
        minimo = num

    if num%2 == 0:
        soma_pares += num
        cont_pares += 1

    soma += num
    cont += 1

media  = soma/cont
media_pares = soma_pares/cont_pares

print(f"A soma dos números digitados é {soma}.")
print(f"A quantidade de números digitados é {cont}.")
print(f"A média dos números digitados é {media}.")
print(f"O maior número digitado foi {maximo}.")
print(f"O menor número digitado foi {minimo}.")
print(f"A média dos números pares é {media_pares}.")
