'''
Faça um algoritmo que encontre o primeiro múltiplo de 11, 13 ou 17 após um número dado.
'''

num = int(input("Digite um número: "))
i = num

while True:
    if i%11 == 0:
        print(f"{i} é o primeiro múltiplo de 11 do número {num}.")
        break
    elif i%13 == 0:
        print(f"{i} é o primeiro múltiplo de 13 do número {num}.")
        break
    elif i%17 == 0:
        print(f"{i} é o primeiro múltiplo de 17 do número {num}.")
        break
    else:
        i += 1
