'''
Escreva uma função que retorne a primeira posição de uma sub-string dentro de uma string. Caso a sub-string
não seja encontrada, a função deve retornar -1.
'''

def posicao(string, substring):
    for i in range(len(string)+1):
        for j in range(i, len(string)+1):
            if substring == string[i:j]:
                return f'A sub-string está na posição {i} da string.'
    return -1

print(posicao('Caramba, que coisa é essa', 'ue coia'))
print(posicao('Caramba, que coisa é essa', 'ue coi'))
