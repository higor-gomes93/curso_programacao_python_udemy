'''
Ler dois conjuntos de números reais, armazenando-os em vetores e calcular o produto escalar entre eles. Os conjuntos
têm 5 elementos cada. Imprimir os dois conjuntos e o produto escalar, sendo que o produto escalar é dado por:
x1*y1 + x2*y2 + ... + xn*yn.
'''

vetor_a = []
vetor_b = []
vetor_c = []
i = 0

while len(vetor_a) < 5:
    num = float(input(f'Digite o {len(vetor_a)+1}º número do vetor a: '))
    vetor_a.append(num)

while len(vetor_b) < 5:
    num = float(input(f'Digite o {len(vetor_b)+1}º número do vetor b: '))
    vetor_b.append(num)

while i < 5:
    num = vetor_a[i]*vetor_b[i]
    vetor_c.append(num)
    i += 1

print(f'Conjunto 1: {vetor_a}\nConjunto 2: {vetor_b}\nProduto Escalar: {vetor_c}')
