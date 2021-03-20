'''
Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado das componentes deste vetor,
armazenando o resultado em outro vetor. Os conjuntos têm 10 elementos cada. Imprimir todos os conjuntos.
'''

lista = []
lista_quadrado = []
cont = 0

while cont < 10:
    num = float(input("Digite um número real: "))
    num_quad = num**2
    lista.append(num)
    lista_quadrado.append(num_quad)
    cont += 1

print(lista)
print(lista_quadrado)
