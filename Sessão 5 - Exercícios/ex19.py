'''
Faça um programa para verificar se um determinado número inteiro é divisível por 3 ou por 5,
mas não simultaneamente pelos dois.
'''

num_1 = int(input("Digite um numero inteiro: "))

if not (num_1%3 == 0 and num_1%5 == 0):
    if num_1%3 == 0:
        print("O numero eh divisivel por 3, mas nao por 5")
    elif num_1%5 == 0:
        print("O numero eh divisivel por 5, mas nao por 3")
    else:
        print("O numero nao eh divisivel por 3 ou 5")
else:
    print("O numero eh divisivel por 3 e 5 simultaneamente")

