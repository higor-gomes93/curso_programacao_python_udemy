'''
Leia uma matriz 5 x 5. Leia também um valor X. O programa deverá fazer uma busca desse valor na matriz e, ao final,
escrever a localização (linha e coluna) ou uma mensagem de "não encontrado".
'''

import random
numero = random.randint(1, 50)

matriz = [[random.randint(1, 50) for j in range(5)] for i in range(5)]
list(map(lambda x: print(*matriz[x]), range(5)))

def procurar(elemento):
    for i in range(5):
        for j in range(5):
            if elemento[i][j] == numero:
                return f'O valor {numero} está na linha {i+1} e coluna {j+1}'
    return f'O número {numero} não foi encontrado'
    
print(procurar(matriz))
