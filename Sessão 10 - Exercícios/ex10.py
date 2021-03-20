'''
Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos 
existentes entre 1 e um número inteiro informado pelo usuário.
'''

lista = ([j for j in range(1, i+1) if i%j == False] for i in range(1, int(input('Limite: '))+1))
print(list(map(lambda x: max(x), filter(lambda x: len(x) == 2, lista))))
