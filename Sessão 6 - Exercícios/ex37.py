'''
Escreva um programa que verifique quais números entre 1000 e 9999 (inclusive) possuem a seguinte
propriedade: a soma dos dois dígitos de mais baixa ordem com os dois dígitos de mais alta ordem
elevada ao quadrado é igual ao próprio número.
'''

for i in range(1000, 10000):
    i = str(i)
    alg_1 = int(i[0:2])
    alg_2 = int(i[2:4])
    conta_1 = alg_1 + alg_2
    conta_2 = conta_1**2
    i = int(i)
    if i == conta_2:
        print(f"O valor {i} obedece à regra.")
