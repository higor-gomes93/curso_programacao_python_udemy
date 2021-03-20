'''
Escreva um programa que leia o número de habitantes de uma determinada cidade, o valor do kwh, e para
cada habitante entre com os seguintes dados: consumo do mês e o código do consumidor (1-Residencial, 
2-Comercial, 3-Industrial). No final imprima o maior, o menor e a média do consumo dos habitantes; e
por fim o total do consumo de cada categoria de consumidor.
'''

hab = int(input("Digite o número de habitantes na cidade: "))
kwh = float(input("Digite o preço do kwh: "))

cont = 1
soma_total = 0
soma_resid = 0
soma_comerc = 0
soma_indust = 0
pessoa_min = 0
pessoa_max = 0

while cont <= hab:
    categoria = int(input(f"Digite a categoria do habitante {cont}:\n1-Residencial\n2-Comercial\n3-Industrial\n- "))
    gasto = float(input(f"Digite o consumo do habitante {cont}: "))
    consumo = gasto*kwh
    
    if cont == 1:
        maximo = consumo
        minimo = consumo

    if consumo >= maximo:
        maximo = consumo
        pessoa_max = cont
    elif consumo <= minimo:
        minimo = consumo
        pessoa_min = cont
    
    if categoria == 1:
        soma_resid += consumo
    elif categoria == 2:
        soma_comerc += consumo
    elif categoria == 3:
        soma_indust += consumo
    
    soma_total += consumo
    cont += 1

media = soma_total/(cont-1)

print(f"O maior consumo foi {maximo}, referente ao habitante {pessoa_max}.")
print(f"O menor consumo foi {minimo}, referente ao habitante {pessoa_min}.")
print(f"A média do consumo total foi {media}.")
print(f"O consumo por categoria foi:\n1-{soma_resid}\n2-{soma_comerc}\n3-{soma_indust}")
