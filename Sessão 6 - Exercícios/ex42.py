'''
Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e escreva para
cada um dos valores lidos o quadrado, o cubo e a raiz quadrada. Finalize a entrada de dados com
um valor negativo ou zero.
'''

num = float(input("Insira um número: "))

while num > 0:
    print(f"O quadrado de {num} é {num**2}.")
    print(f"O cubo de {num} é {num**3}.")
    print(f"A raiz quadrada de {num} é {num**0.5}.")
    num = float(input("Insira um número: "))
