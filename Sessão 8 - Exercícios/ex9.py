'''
Faça uma função que receba a altura e o raio de um cilindro circular e retorne o volume do cilindro. O volume de um
cilindro é calculado por meio da seguinte fórmula: V = pi*raio^2*altura, onde pi = 3.141592.
'''

def vol_cilindro(altura, raio):
    return round((3.141592)*altura*(raio**2), 2)

print(vol_cilindro(4, 2))
