'''
Fazer um programa para ler 5 valores e, em seguida, mostrar a posição onde se encontram o maior e o
menor valor.
'''

valores = []

while len(valores) < 5:
    valor = float(input('Digite um número: '))
    valores.append(valor)

print('-' * 80)
print(f"Lista completa: {valores}")
print(f"O maior valor está na posição {valores.index(max(valores))}.")
print(f"O menor valor está na posição {valores.index(min(valores))}.")
