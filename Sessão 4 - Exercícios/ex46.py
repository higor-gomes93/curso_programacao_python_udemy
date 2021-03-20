'''
Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999). Gere outro número
formado pelos dígitos invertidos do número lido.
'''

entrada = input("Digite um numero com 3 digitos: ")
saida = entrada[::-1]
print(f"O inverso eh {saida}")