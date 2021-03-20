'''
Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo em vista que o
desconto foi de 12%.
'''

valor = float(input("Insira o valor do produto: "))
desconto = 0.12*valor
valor_final = valor - desconto
print(f"O valor com desconto eh de R$ {valor_final}")