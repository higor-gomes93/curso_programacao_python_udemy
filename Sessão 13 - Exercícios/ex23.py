'''
Escreva um programa que leia a profissão e o tempo de serviço (em anos) de cada um dos 5
funcionários de uma empresa e armazene-os no arquivo "emp.txt". Cada linha do arquivo
corresponde aos dados de um funcionário.
'''

raiz = 'c:/Users/Higor H/Documents/Estudos/Python'
pasta = raiz + '/Curso de Programação em Python (Udemy)/Sessão 13 - Exercícios/ex23.txt'

with open(pasta, 'w', encoding='UTF-8') as arquivo:
    for i in range(5):
        nome = input('Digite o nome: ')
        cargo = input('Digite o cargo: ')
        tempo = input('Digite o tempo de serviço: ')
        arquivo.write(f'Nome: {nome} - Cargo: {cargo} - Tempo de Empresa: {tempo}\n')
