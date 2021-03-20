'''
Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lidos.
'''

valor_um = float(input("Coloque o primeiro valor: "))
valor_dois = float(input("Coloque o segundo valor: "))
valor_tres = float(input("Coloque o terceiro valor: "))

calculo = (valor_um**2) + (valor_dois**2) + (valor_tres**2)

print(f"A soma dos quadrados dos valores eh {calculo}")