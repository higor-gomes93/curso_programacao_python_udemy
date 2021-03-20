'''
Leia um valor em real e a cotação do dolar. Em seguida, imprima o valor correspondente em dolares.
'''

valor_real = float(input("Insira a quantia em real: "))
valor_dolar = 4.19
cambio = round((valor_real/valor_dolar), 2)

print(f"O valor corresponde a {cambio} dolares")