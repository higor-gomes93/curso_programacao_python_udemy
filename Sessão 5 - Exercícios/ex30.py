'''
Faça um programa que receba três números e os mostre em ordem crescente.
'''

num_1 = float(input("Digite o primeiro numero: "))
num_2 = float(input("Digite o segundo numero: "))
num_3 = float(input("Digite o terceiro numero: "))

# Encontrando o primeiro
if num_1 >= num_2 and num_1 >= num_3:
    primeiro = num_1
elif num_2 >= num_1 and num_2 >= num_3:
    primeiro = num_2
elif num_3 >= num_1 and num_3 >= num_2:
    primeiro = num_3

# Encontrando o segundo
if (num_1 >= num_2 and num_1 <= num_3) or (num_1 <= num_2 and num_1 >= num_3):
    segundo = num_1
elif (num_2 >= num_1 and num_2 <= num_3) or (num_2 <= num_1 and num_2 >= num_3):
    segundo = num_2
elif (num_3 >= num_1 and num_3 <= num_2) or (num_3 <= num_1 and num_3 >= num_2):
    segundo = num_3

# Encontrando o primeiro
if num_1 <= num_2 and num_1 <= num_3:
    terceiro = num_1
elif num_2 <= num_1 and num_2 <= num_3:
    terceiro = num_2
elif num_3 <= num_1 and num_3 <= num_2:
    terceiro = num_3

print(f"Os numeros, em ordem crescente, sao {terceiro}, {segundo}, {primeiro}")


