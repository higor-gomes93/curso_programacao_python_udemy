'''
Faça uma função que receba como parâmetro o valor de um ângulo em graus e calcule o valor do coseno hiperbólico
desse ângulo usando sua respectiva série de Taylor. Considerar pi = 3.141593 e n variando de 0 a 5.
'''

import math as m

def serie_taylor(numero):
    numero = (3.141593)*numero/180
    cosenoh = 0
    for i in range(0, 6):
        cosenoh += (numero**(2*i))/m.factorial(2*i)
    return round(cosenoh, 3)

print(serie_taylor(30))
