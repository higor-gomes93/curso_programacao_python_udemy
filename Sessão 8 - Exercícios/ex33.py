'''
Faça uma função que receba um número N e retorne a soma dos algarismos de N!.
'''

def soma_fatorial(numero):
    fatorial = 1
    soma = 0
    for i in range(1, numero+1):
        fatorial *= i
    fatorial = str(fatorial)
    for i in fatorial:
        i = int(i)
        soma += i
    return f'A soma dos algarismos de {fatorial} é {soma}'

print(soma_fatorial(6))
