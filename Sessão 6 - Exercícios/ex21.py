'''
Faça um programa que receba dois números. Calcule e mostre:
    - a soma dos números pares desse intervalo de números, incluindo os números digitados;
    - a multiplicação dos números ímpares desse intervalo, incluindo os digitados.
'''

num_1 = int(input("Digite o limite inferior do intervalo: "))
num_2 = int(input("Digite o limite superior do intervalo: "))
soma = 0
mult = 1

for i in range(num_1, num_2+1):
    if i%2 == 0 or i == 0:
        soma = soma + i
    elif i%2 != 0:
        mult = mult*i

print(f"A soma dos números pares vale {soma} e a multiplicação dos números ímpares vale {mult}.")
