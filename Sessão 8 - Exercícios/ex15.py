'''
Crie um programa que receba três valores (obrigatoriamente maiores que zero), representando as medidas dos três
lados de um triângulo. Elabore funções para:
- Determinar se esses lados formam um triângulo;
- Determinar e mostrar o tipo de triângulo.
'''

def check_triangulo(lado1, lado2, lado3):
    if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
        return 'É um triângulo'
    return 'Não é um triângulo'

def tipo_triangulo(lado1, lado2, lado3):
    if lado1 != lado2 != lado3:
        return 'É um triângulo escaleno.'
    elif lado1 == lado2 != lado3  or lado1 == lado3 != lado2 or lado2 == lado3 != lado1:
        return 'É um triângulo isósceles.'
    elif lado1 == lado2 == lado3:
        return 'É um triângulo equilátero.'

print(check_triangulo(3, 4, 5))
print(tipo_triangulo(3, 4, 5))
print(tipo_triangulo(3, 3, 3))
print(check_triangulo(3, 4, 4))
print(tipo_triangulo(3, 4, 4))
