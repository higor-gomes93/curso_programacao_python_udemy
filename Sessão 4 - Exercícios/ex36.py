'''
Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume do cilindro circular é
calculado por meio da seguinte fórmula: V =  pi*(raio^2)*altura, onde pi = 3.141592.
'''

altura = float(input("Digite a altura do cilindro, em milimetros: "))
raio = float(input("Digite o raio do cilindro, em milimetros: "))
pi = 3.141592
volume = pi*(raio**2)*altura
print(f"O volume do cilindro eh de {volume} milimetros cubicos.")