'''
Faça um programa que apresente um menu de opções para o cálculo das seguintes operações entre
dois números:
- Adição (opção 1)
- Subtração (opção 2)
- Multiplicação (opção 3)
- Divisão (opção 4)
- Saída (opção 5)
'''

while True:
    print("Escolha uma das opções:\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Sair")
    option = input()
    if option == "5":
        print("Até mais!")
        break
    elif option == "1":
        num_1 = float(input("Digite um número: "))
        num_2 = float(input("Digite outro número: "))
        conta = num_1 + num_2
        print(f"O resultado para {num_1} + {num_2} é {conta}.")
    elif option == "2":
        num_1 = float(input("Digite um número: "))
        num_2 = float(input("Digite outro número: "))
        conta = num_1 - num_2
        print(f"O resultado para {num_1} - {num_2} é {conta}.")
    elif option == "3":
        num_1 = float(input("Digite um número: "))
        num_2 = float(input("Digite outro número: "))
        conta = num_1 * num_2
        print(f"O resultado para {num_1} x {num_2} é {conta}.")
    elif option == "4":
        num_1 = float(input("Digite um número: "))
        num_2 = float(input("Digite outro número: "))
        conta = num_1 / num_2
        print(f"O resultado para {num_1} / {num_2} é {conta}.")
    else:
        print("Opção inválida.")
