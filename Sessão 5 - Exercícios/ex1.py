'''
Faça um programa que receba dois números e mostre qual deles é o maior.
'''

num1 = input("Digite um numero: ")
num2 = input("Digite mais um: ")

if num1 > num2:
    print("O primeiro numero eh maior que o segundo.")
elif num1 == num2:
    print("Os dois numeros sao iguais.")
else:
    print("O segundo numer o eh maior que o primeiro.")