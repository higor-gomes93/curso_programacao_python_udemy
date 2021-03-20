'''
Crie uma função que receba como parâmetro um valor inteiro e gere como saída n linhas com pontos de exclamação.
'''

def printa_exclamacao(linhas):
    for i in range(1, linhas+1):
        print('!'*i)
    return

printa_exclamacao(5)
