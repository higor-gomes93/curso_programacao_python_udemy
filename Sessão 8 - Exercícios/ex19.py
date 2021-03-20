'''
Faça uma função que retorne o maior fator primo de um número.
'''

def fator_primo(numero):
    primos = []
    cont = 0
    for i in range(1, numero + 1):
        if numero%i == 0:
            for j in range(1, i+1):
                if i%j == 0:
                    cont += 1
            if cont < 3:
                primos.append(i)
            cont = 0       
    return max(primos)

print(fator_primo(21))
