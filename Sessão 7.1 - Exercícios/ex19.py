'''
Faça um vetor de tamanho 50 preenchido com o seguinte valor: (i+5*i)%(i+1), sendo i a posição do elemento no vetor.
Em seguida, imprima o vetor na tela.
'''

vetor = []
i = 0
num = (i+(5*i))%(i+1)

while i < 50:
    num = (i+(5*i))%(i+1)
    vetor.append(num)
    i += 1

print(vetor)
