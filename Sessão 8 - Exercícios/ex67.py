'''
Faça uma rotina que receba como parâmetro um vetor de caracteres e seu tamanho. A função deverá ler uma string
do teclado, caractere por caractere, até que o usuário digite enter ou o tamanho máximo do vetor seja alcançado.
'''

def getchar(*args, tamanho=0):
    vetor = list(args)
    if tamanho == 0:
        return 'Nada a retornar.'
    if len(vetor) < tamanho:
        return vetor
    elif len(vetor) >= tamanho:
        return vetor[:tamanho]

caracteres = input('Digite os caracteres desejados: ')
print(caracteres)
print(getchar(*caracteres, tamanho=10))
