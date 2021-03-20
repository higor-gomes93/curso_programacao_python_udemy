'''
Faça uma função que imprima um caracter um certo número de vezes.
'''

def decoradora(*tipos):
    def pega_funcao(function):
        def tratamento(*args, **kwargs):
            argumentos = []
            for (tipo, valor) in zip(tipos, args):
                argumentos.append(tipo(valor))
            return function(*argumentos, **kwargs)
        return tratamento
    return pega_funcao


@decoradora(str, int)
def imprimir(caracter, vezes):
    return print(caracter*vezes)

imprimir('*', 6)
