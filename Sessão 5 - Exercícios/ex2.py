'''
Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do
número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
'''
import math as m

num = float(input("Digite um numero positivo: "))

if num > 0:
    raiz = m.sqrt(num)
    print(f"A raiz quadrada do numero eh {m.sqrt(num)}")
    print(f"A raiz quadrada do numero eh {raiz}.")
else:
    print("O numero eh invalido.")