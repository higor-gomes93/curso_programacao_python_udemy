'''
Faça um programa que some os números ímpares contidos em um intervalo definido pelo usuário.
O usuário define o valor inicial do intervalo e o valor final deste intervalo e o programa
deve somar todos os números ímpares contidos neste intervalo. Caso o usuário digite um
intervalo inválido (começando por um valor maior que o valor final), deve ser escrito uma
mensagem de erro na tela, "Intervalo de valores inválido" e o programa termina.
'''

inicio = int(input("Digite um valor inicial: "))
fim = int(input("Digite um valor final: "))
soma = 0

if inicio <= fim:
    for i in range(inicio, fim+1):
        if i%2 != 0:
            soma = soma + i
else:
    print("Intervalo de valores inválido.")

print(f"Soma dos ímpares neste intervalo: {soma}")
