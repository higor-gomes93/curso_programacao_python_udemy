'''
Faça uma função que some dois elementos a e b apenas se forem números inteiros.
'''

def decorador(function):
    def verificadora(*elementos):
        if all(isinstance(i, int) for i in elementos):
            return function(*elementos)
        else:
            return 'Valores incorretos, precisam ser inteiros.'
    return verificadora

@decorador
def soma(*elementos):
    return sum(elementos)

print(soma(4, 2, 3, 1))
