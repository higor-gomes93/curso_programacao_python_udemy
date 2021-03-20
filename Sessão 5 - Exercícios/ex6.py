'''
Escreve um programa que, dados dois números inteiros, mostre na tela o maior deles, assim como a 
diferença existente entre ambos.
'''

num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite outro numero inteiro: "))

if num1 > num2:
    print(f"O numero {num1} eh maior que o numero {num2}")
else:
    print(f"O numero {num2} eh maior que o numero {num1}")

dif = num1 - num2
absoluto = abs(dif)
print(f"A diferença entre os numeros eh {absoluto}")