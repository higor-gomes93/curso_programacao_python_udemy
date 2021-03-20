'''
Ler dois conjuntos de números reais, armazenando-os em vetores e calcular o produto escalar entre eles. Os conjuntos
têm 5 elementos cada. Imprimir os dois conjuntos e o produto escalar, sendo que o produto escalar é dado por:
x1*y1 + x2*y2 + ... + xn*yn.
'''

conj1 = [float(input(f'Digite o {x+1}º número do conjunto 1: ')) for x in range(5)]
conj2 = [float(input(f'Digite o {x+1}º número do conjunto 2: ')) for x in range(5)]

conjunto = [conj1, conj2]

res = [conjunto[0][i]*conjunto[1][i] for i in range(5)]
print(f'Produto escalar: {res}')
