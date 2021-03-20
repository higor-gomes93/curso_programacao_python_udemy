'''
Faça uma função não-recursiva que receba um número inteiro positivo n e retorne o superfatorial desse número. O 
superfatorial de um número N é definido pelo produto dos N primeiros fatoriais de N.
'''

def superfatorial(numero):
    produto = 1
    fatorial = 1
    for i in range(1, numero+1):
        for j in range(1, i+1):
            produto *= j
        fatorial *= produto
        produto = 1
    return fatorial

print(superfatorial(4))
