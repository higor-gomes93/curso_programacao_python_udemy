'''
Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação: hip = sqrt(a^2 + b^2). Faça
uma função que receba os valores de a e b e calcule o valor da hipotenusa através da equação.
'''

import math

def hipotenusa(a, b):
    return round(math.sqrt(a**2 + b**2), 2)

print(hipotenusa(3, 4))
