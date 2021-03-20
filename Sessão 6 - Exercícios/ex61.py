'''
Faça um programa que calcule o maior número palíndromo feito a partir do produto de dois números
de 3 dígitos.
'''

for i in range (100, 1000):
    for j in range(100, 1000):
        num = i*j
        num = str(num)
        inv_num = num[::-1]
        if num == inv_num:
            palindromo = num
            alg_1 = i
            alg_2 = j

print(f"Os algarismos são {alg_1} e {alg_2}, e o palíndromo é {palindromo}.")
