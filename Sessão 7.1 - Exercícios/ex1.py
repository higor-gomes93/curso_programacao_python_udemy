'''
Faça um programa que possua um vetor denominado A e que armazene 6 números inteiros. O programa deve
executar os seguintes passos:
(a) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7.
(b) Armazene em uma variável inteira (simples) a soma entre os valores das posições A[0], A[1] e A[5]
do vetor e mostre a soma na tela.
(c) Modifique o vetor na posição 4, atribuindo a esta posição o valor 100.
(d) Mostre na tela cada valor do vetor A, um em cada linha.
'''

vetor_a = []

# Item a
vetor_a.extend([1, 0, 5, -2, -5, 7])  # Poderia ter sido utilizado o .append(), mas ele add 1 item por vez
print(vetor_a)

# Item b
soma = vetor_a[0] + vetor_a[1] + vetor_a[5]
print(soma)

# Item c
vetor_a[4] = 100
print(vetor_a)

# Item c
for elemento in vetor_a:
    print(elemento)
