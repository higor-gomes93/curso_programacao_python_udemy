'''
Faça um programa que calcule a diferença entre a soma dos quadrados dos primeiros 100 números naturais
e o quadrado da soma.
'''

num = int(input("Inisira a quantidade de números naturais: "))  # Inserir o valor 100
soma_1 = 0
soma_2 = 0

for i in range(1, num+1):
    soma_1 = soma_1 + i
    soma_2 = soma_2 + i**2

resultado = (soma_1**2) - soma_2
final = abs(resultado)

print(f"O resultado é {final}.")
