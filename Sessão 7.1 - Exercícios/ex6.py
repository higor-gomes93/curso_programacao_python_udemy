'''
Faça um programa que receba do usuário um vetor com 10 posições. Em seguida deverá ser impresso o maior
e o menor elemento do vetor.
'''

lista =[]

while len(lista) < 10:
    num = float(input("Digite um valor: "))
    lista.append(num)

print(lista)
print(f"O valor máximo vale {max(lista)} e o valor mínimo vale {min(lista)}.")
