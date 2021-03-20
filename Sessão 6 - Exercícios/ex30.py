'''
Faça programas para calcular as seguintes sequências:
a) 1 + 2 + 3 + 4 + 5 + ... + n
b) 1 - 2 + 3 - 4 + 5 + ... + (2n-1)
c) 1 + 3 + 5 + 7 + ... + (2n-1)
'''

num = int(input("Digite um número: "))

soma_1 = 0
soma_2 = 0
soma_3 = 0

for i in range(1, num+1):
    soma_1 = soma_1 + i

for i in range(1, num+1):
    if i%2 == 0:
        i = - i
    else:
        i = i
    soma_2 = soma_2 + i

for i in range(1, num+1):
    if i%2 != 0:
        soma_3 = soma_3 + i

print(f"Sequência 1: {soma_1}.")
print(f"Sequência 2: {soma_2}.")
print(f"Sequência 3: {soma_3}.")
