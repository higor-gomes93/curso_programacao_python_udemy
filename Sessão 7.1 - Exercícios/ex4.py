'''
Faça um programa que leia um vetor de 8 posições e, em seguida, leia também dois valores X e Y quaisquer
correspondentes a duas posições no vetor. Ao final, seu programa deverá escrever a soma dos valores
encontrados nas respectivas posições X e Y.
'''

lista = []

while len(lista) < 8:
    num = float(input("Digite um número: "))
    lista.append(num)

pos_x = 10
pos_y = 10

while pos_y not in range(0,8) or pos_x not in range(0,8):
    pos_x = int(input("Digite a posição X: "))
    pos_y = int(input("Digite a posição Y: "))

soma = lista[pos_x] + lista[pos_y]
print(lista)
print(f"A soma dos itens na posição {pos_x} e {pos_y} vale {soma}.")
