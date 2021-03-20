'''
Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação: hipotenusa = raiz(a^2 + b^2). Faça
um programa que receba os valores de a e b e calcule o valor da hipotenusa através da equação. Imprima o resultado
dessa operação.
'''

# Primeira maneira
a = float(input("Insira o valor do cateto oposto: "))
b = float(input("Insira o valor do cateto adjacente: "))
hipotenusa = ((a**2) + (b**2))**(0.5)
print(f"A hipotenusa vale {hipotenusa}")

# Segunda maneira
import math

a = float(input("Insira o valor do cateto oposto: "))
b = float(input("Insira o valor do cateto adjacente: "))
hipotenusa = math.sqrt((a**2) + (b**2))
print(f"A hipotenusa vale {hipotenusa}")
