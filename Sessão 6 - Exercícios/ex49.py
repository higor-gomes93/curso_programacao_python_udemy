'''
Um funcionário chamado Carlos tem um colega chamado João que recebe um salário que equivale a um terço
do seu salário. Carlos gosta de fazer aplicações na caderneta de poupança e vai aplicar seu salário
integralmente nela, pois está rendendo 2% ao mês. João aplicará seu salário integralmente no fundo de
renda fixa, que está rendendo 5% ao mês. Construa um programa que deverá calcular e mostrar a quantidade
de meses necessários para que o valor pertencente a João iguale ou ultrapasse o valor pertencente a
Carlos. Teste com outros valores para as taxas.
'''

salario_carlos = 3
salario_joao = 1
i_carlos = 0.02
i_joao = 0.05
n = 1

# valor_futuro = salario*(1+i)*((((1+i)**n)-1)/i)

valor_futuro_carlos = 3
valor_futuro_joao = 1

while valor_futuro_joao < valor_futuro_carlos:
    valor_futuro_joao = salario_joao*(1+i_joao)*((((1+i_joao)**n)-1)/i_joao)
    valor_futuro_carlos = salario_carlos*(1+i_carlos)*((((1+i_carlos)**n)-1)/i_carlos)
    n += 1

print(f"Serão necessário {n} meses para o montante de João ultrapassar o de Carlos.")
