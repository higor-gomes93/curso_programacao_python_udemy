'''
Faça um programa que some todos os números naturais abaixo de 1000 que são múltiplos de 3 ou 5.
'''

num = int(input("Insira um número: "))  # Inserir o número 1000
soma = 0

for i in range(num, -1, -1):
    if i%3 == 0 or i%5 == 0:
        soma += i 

print(f"A soma de todos os números abaixo de {num}, e que são múltiplos de 3 ou 5, é {soma}.")
