'''
Faça uma função que some dois elementos a e b apenas se forem números inteiros, passando por parâmetro.
'''
def decorador(tipo):
    def pega_funcao(function):
        def verificadora(*elementos):
            if all(isinstance(i, tipo) for i in elementos):
                return function(*elementos)
            else:
                return 'Valores incorretos, precisam ser inteiros.'
        return verificadora
    return pega_funcao

@decorador(int)
def soma(*elementos):
    return sum(elementos)

print(soma(4, 'a', 3, 1))