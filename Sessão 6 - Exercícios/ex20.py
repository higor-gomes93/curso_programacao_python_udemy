'''
Ler uma sequência de números inteiros e determinar se eles são pares ou não. Deverá ser informado
o número de dados lidos e números de valores pares. O processo termina quando for digitado o
número 1000.
'''

print("Olá! Vamos analisar sua sequência numérica. Digite 1000 se quiser parar.")
num = int(input("Digite o número a ser analisado: "))
cont = 0
total = 0

while num != 1000:
    if num%2 == 0:
        cont = cont + 1
    total = total + 1
    num = int(input("Digite o número a ser analisado: "))

print(f"Analisamos {total} números e {cont} são par.")
