'''
Faça um programa que receba como entrada o ano corrente e o nome de dois arquivos:
um de entrada e outro de saída. Cada linha do arquivo de entrada contém o nome de
uma pessoa e o seu ano de nascimento. O programa deverá ler o arquivo de entrada
e gerar um arquivo de saída onde aparece o nome da pessoa seguida por uma string
que representa sua idade.
- Se a idade for menor do que 18 anos, escreva "menor de idade"
- Se a idade for maior do que 18 anos, escreva "maior de idade"
- Se a idade for igual a 18 anos, escreva "entrando na maioridade"
'''

raiz = 'c:/Users/Higor H/Documents/Estudos/Python'
pasta1 = raiz + '/Curso de Programação em Python (Udemy)/Sessão 13 - Exercícios/ex15_1.txt'
pasta2 = raiz + '/Curso de Programação em Python (Udemy)/Sessão 13 - Exercícios/ex15_2.txt'
ano_atual = 2020
dicionario = {}

with open(pasta1, 'r', encoding='UTF-8') as arquivo:
    lista = arquivo.readlines()
    for i in lista:
        informacao = i.split()
        nome = ''
        ano_nascimento = int(informacao[-1])
        for j in informacao:
            if j != '-':
                nome += f'{j} '
            else:
                break
        dicionario[nome.strip()] = ano_nascimento

with open(pasta2, 'w', encoding='UTF-8') as arquivo:
    for nome, ano in dicionario.items():
        if ano_atual - ano > 18:
            arquivo.write(f'{nome} é maior de idade.\n')
        elif ano_atual - ano < 18:
            arquivo.write(f'{nome} é menor de idade.\n')
        elif ano_atual - ano == 18:
            arquivo.write(f'{nome} está entrando na maioridade.\n')
        else:
            arquivo.write(f'{nome} está viajando no tempo.\n')
