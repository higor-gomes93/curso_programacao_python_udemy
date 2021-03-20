'''
Elabore um função que receba três notas de um aluno como parâmetros e uma letra. Se a letra for A, a função
deverá calcular a média aritmética das notas dos alunos; se for P, deverá calcular a média ponderada com 
pesos 5, 3 e 2.
'''

def media(nota1, nota2, nota3, categoria='A'):
    if categoria == 'A':
        return (nota1 + nota2 + nota3)/3
    elif categoria == 'P':
        return (nota1*5 + nota2*3 + nota3*2)/10
    return 'Categoria inválida.'

print(media(1, 1, 1))
print(media(1, 1, 1, 'A'))
print(media(1, 1, 1, 'P'))
print(media(2, 3, 5))
print(media(3, 2, 1, 'G'))
