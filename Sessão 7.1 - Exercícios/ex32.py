'''
Leia dois vetores inteiros x e y, cada um com 5 elementos (assuma que o usuário não informa números repetidos).
Calcule e mostre os vetores resultantes em cada caso abaixo:
- Soma entre x e y: soma de cada elemento de x com o elemento da mesma posição em y
- Produto entre x e y: multiplicação de cada elemento de x com o elemento da mesma posição em y
- Diferença entre x e y: todos os elementos de x que não existam em y
- Intersecção entre x e y: apenas os elementos que aparecem nos dois vetores
- União entre x e y: todos os elementos de x, e todos os elementos de y que não estão em x.
'''

# Aquisição dos dados
vetor_x = []
vetor_y = []

while len(vetor_x) < 5:
    num = int(input(f'Digite o {len(vetor_x)+1}º número do vetor x: '))
    if num not in vetor_x:
        vetor_x.append(num)

while len(vetor_y) < 5:
    num = int(input(f'Digite o {len(vetor_y)+1}º número do vetor y: '))
    if num not in vetor_y:
        vetor_y.append(num)

print(f'Vetor x: {vetor_x}.')
print(f'Vetor y: {vetor_y}.')

# Calculando a soma
vetor_soma = []
i = 0
while i < 5:
    num = vetor_x[i] + vetor_y[i]
    vetor_soma.append(num)
    i += 1
print(f'A soma entre x e y vale {vetor_soma}.')

# Calculando o produto
vetor_produto = []
i = 0
while i < 5:
    num = vetor_x[i] * vetor_y[i]
    vetor_produto.append(num)
    i += 1
print(f'O produto entre x e y vale {vetor_produto}.')

# Transformando em conjuntos
conjunto_x = set(vetor_x)
conjunto_y = set(vetor_y)

# Calculando a diferença
vetor_diferença = conjunto_x.difference(conjunto_y)
vetor_diferença = list(vetor_diferença)
print(f'A diferença entre x e y vale {vetor_diferença}.')

# Calculando a intersecção
vetor_interseccao = conjunto_x.intersection(conjunto_y)
vetor_interseccao = list(vetor_interseccao)
print(f'A intersecção entre x e y vale {vetor_interseccao}.')

# Calculando a união
vetor_uniao = conjunto_x.union(conjunto_y)
vetor_uniao = list(vetor_uniao)
print(f'A união entre x e y vale {vetor_uniao}.')
