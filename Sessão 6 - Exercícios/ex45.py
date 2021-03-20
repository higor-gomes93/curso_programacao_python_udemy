'''
Faça um algoritmo que converta uma velocidade expressa em km/h para m/s e vice versa. Você deve criar
um menu com as duas opções de conversão e com uma opção para finalizar o programa. O usuário poderá
fazer quantas conversões desejar, sendo que o programa só será finalizado quando a opção de finalizar
for escolhida.
'''

while True:
    print("Olá! Escolha uma das opções abaixo:")
    print("A - Converter de km/h para m/s\nB - Converter de m/s para km/h\nC - Sair")
    tipo = input()
    if tipo == "A":
        velo = float(input("Digite uma velocidade em km/h: "))
        conv = velo/3.6
        print(f"A velocidade é {conv} m/s.")
    elif tipo == "B":
        velo = float(input("Digite uma velocidade em m/s: "))
        conv = velo*3.6
        print(f"A velocidade é {conv} km/h.")
    elif tipo == "C":
        break

print("Obrigado!")
