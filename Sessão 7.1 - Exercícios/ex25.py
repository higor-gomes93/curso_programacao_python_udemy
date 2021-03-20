'''
Faça um programa que preencha um vetor de tamanho 100 com os 100 primeiros naturais que não são múltiplos de 7
ou que terminam com 7.
'''

vetor = [0]
tupla = (17, 27, 37, 47, 57, 67, 77, 87, 97)
i = 1

while len(vetor) < 100:
    num = i
    if num%7 != 0 and not(num in tupla):
        vetor.append(num)
    i += 1

print(vetor)
