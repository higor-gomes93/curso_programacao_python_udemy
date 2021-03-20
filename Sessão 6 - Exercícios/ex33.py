'''
Dados n e dois números inteiros positivos, i e j, diferentes de 0, imprimir em ordem crescente os
n primeiros naturais que são múltiplos de i ou de j e ou de ambos.
'''

num = int(input("Digite o número n: "))
mult_1 = int(input("Digite o número i: "))
mult_2 = int(input("Digite o número j: "))
cont = 0
i = 0

while cont < num:
    if (i%mult_1 == 0) or (i%mult_2 == 0) or (i%mult_1 == 0 and i%mult_2 == 0):
        print(i, end =" ")
        cont = cont + 1
    i = i + 1
