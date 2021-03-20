'''
O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, 
que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela
de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário.
'''

valorpao = float(input('Qual o valor do pão? '))
tabela = list(map(lambda x: x*valorpao, range(1, 51)))
print(f'\nPreço do pão: R$ {valorpao}\nPanificadora Pão de Ontem - Tabela de preços')
[print(f'{tabela.index(i)+1} - R$ {round(i, 2)}') for i in tabela]
