'''
Faça um programa que peça ao usuário para digitar 10 valores e some-os.
'''

# Usando o loop for
soma = 0
for n in range(1, 11):
    num = int(input(f"Digite o numero {n}: "))
    soma = soma + num
print(f"A soma final eh {soma}")

# Usando o loop while
soma = 0
n = 1
while n < 11:
    num = int(input(f"Digite o numero {n}: "))
    soma = soma + num
    n += 1
print(f"A soma final eh {soma}")
