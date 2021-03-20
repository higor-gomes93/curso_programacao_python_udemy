'''
Faça um programa que calcule a área de um triângulo, cuja base e altura são fornecidas pelo usuário.
Esse programa não pode permitir entrada de dados inválidos, ou seja, medidas menores ou iguais a 0.
'''
altura = 0
base = 0

while altura <= 0:
    altura = float(input("Digite a altura do triângulo: "))
while base <= 0:
    base = float(input("Digite a base do triângulo: "))

area = (base*altura)/2
print(f"A área do triângulo vale {area}.")
