'''
Faça um programa que leia um vetor de 5 posições para números reais e, depois, um código inteiro. Se o código for zero,
finalize o programa; se for 1, mostre o vetor na ordem direta; se for 2, mostre o vetor na ordem inversa. Caso o código
seja diferente de 1 e 2, escreva uma mensagem informando que o código é inválido.
'''

vetor = []

while len(vetor) < 5:
    num = float(input('Digite um número real: '))
    vetor.append(num)

print('-' * 80)
codigo = int(input('Digite um código:\n0 - Parar\n1 - Ordem Direta do Vetor\n2 - Ordem Inversa do Vetor\n'))
print('-' * 80)

while codigo > 2:
    print('Código Inválido.')
    codigo = int(input('Digite um código\n0 - Parar\n1 - Ordem Direta do Vetor\n2 - Ordem Inversa do Vetor\n'))

if codigo == 0:
    print('Programa Finalizado.')
elif codigo == 1:
    print(f'Vetor: {vetor}.')
elif codigo == 2:
    print(f'Vetor invertido: {vetor[::-1]}.')
