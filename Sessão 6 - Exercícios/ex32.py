'''
Faça um programa que simule o lançamento de dois dados, d1 e d2, n vezes, e tem como saída o número
de cada dado e a relação entre eles (>,<,=) de cada lançamento.
'''
soma = 0
while True:
    start = input("Vamos jogar os dados? ")
    if start != "Não":
        d1 = int(input("Jogue o dado 1: "))
        d2 = int(input("Jogue o dado 2: "))
        if (1<=d1<=6) and (1<=d2<=6):
            if d1 > d2:
                print(f"{d1} é maior que {d2}.")
            elif d2 > d1:
                print(f"{d2} é maior que {d1}.")
            else:
                print(f"{d1} é igual a {d2}.")
            soma = soma + 1
        else:
            print("Números inválidos!")
    else:
        break

print(f"Jogamos os dados {soma} vezes.")
