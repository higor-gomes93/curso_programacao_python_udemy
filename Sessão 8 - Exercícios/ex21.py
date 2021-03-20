'''
Escreva uma função para determinar a quantidade de números primos abaixo de N.
'''

def primos_abaixo(numero):
    primos = []
    cont = 0
    for i in range(1, numero//2 + 1):
        if numero%i == 0:
            for j in range(1, i+1):
                if i%j == 0:
                    cont += 1
            if cont < 3:
                primos.append(i)
            cont = 0
    return len(primos)

print(primos_abaixo(20))
