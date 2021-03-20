'''
Escreva um programa que leia um número inteiro positivo n e em seguida imprima n linhas do chamado
Triângulo de Floyd.
'''

lista = [print(*[j for j in range(sum([indice for indice in range(0, i+1)])+1, 
sum([indice for indice in range(0, i+1)])+(i+2))]) for i in range(0, int(input('Digite um número: ')))]
