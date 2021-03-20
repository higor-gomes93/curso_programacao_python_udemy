'''
Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule e imprima a média geral.
'''

notas = []

for i in range (1, 16):
    nota = float(input(f"Digite a nota do aluno {i}: "))
    notas.append(nota)

media_notas = sum(notas)/15
print(f"A média das notas foi {media_notas}.")
