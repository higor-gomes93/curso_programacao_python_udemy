'''
Um funcionário recebe aumento anual. Em 1995 foi contratado por 2000 reais. Em 1996 recebeu aumento
de 1.5%. A partir de 1997, os aumentos sempre correspondem ao dobro do ano anterior. Faça um programa
que determine o salário atual do funcionário.
'''

salario = 2000
aumento = 0.015*salario
salario = salario + aumento
ano = 1997

while ano <= 2020:
    aumento = 2*aumento
    salario = salario + aumento
    ano += 1

print(f"O salário em 2020 é de {salario}.")
