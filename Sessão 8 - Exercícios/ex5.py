'''
Faça uma função e um programa de teste para o cálculo do volume de uma esfera. Sendo que o raio é passado como
parâmetro.
'''

import math

def sphere_area(radius):
    pi = math.pi
    volume = (4/3)*pi*(radius**3)
    return round(volume, 2)

print(sphere_area(3))
print(sphere_area(4))
