'''
Faça um programa que preencha um vetor com 10 números reais, calcule e mostre a quantidade de números
negativos e a soma dos números positivos desse vetor.
'''

lista = []
total_negativos = 0
positivos = []

while len(lista) < 10:
    num = float(input("Digite um número real: "))
    lista.append(num)

for i in lista:
    if i < 0:
        total_negativos += 1
    elif i > 0:
        positivos.append(i)

print(f"Temos {total_negativos} números negativos e a soma dos positivos vale {sum(positivos)}.")
