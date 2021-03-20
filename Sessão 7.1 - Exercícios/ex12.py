'''
Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos juntamente com o
maior, o menor e a média dos valores.
'''

valores = []

while len(valores) < 5:
    num = float(input('Digite um número: '))
    valores.append(num)

print('-'*100)
print(f"Lista completa: {valores}")
print(f"Maior valor: {max(valores)}")
print(f"Menor valor: {min(valores)}")
print(f"Média dos valores: {sum(valores)/len(valores)}")
