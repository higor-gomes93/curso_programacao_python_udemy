'''
Implemente um controle simples de mercadorias em uma despensa doméstica. Para cada produto
armazene um código numérico, descrição e quantidade atual. O programa deve ter opções para
entrada e retirada de produtos, bem como um relatório geral e um de produtos não disponíveis.
'''

from random import randint
from colorama import *

raiz = 'c:/Users/Higor H/Documents/Estudos/Python'
pasta = raiz + '/Curso de Programação em Python (Udemy)/Sessão 13 - Exercícios/ex24.txt'
init()

def listagem_completa():
    with open(pasta, 'r', encoding='UTF-8') as arquivo:
        dados = arquivo.read().split('\n')
        dados.pop()
        itens = [[j.strip() for j in i.split('-')] for i in dados]
        quantidades = [int(i[2].split().pop(1)) for i in itens]
        for i in range(len(itens)):
            itens[i][2] = quantidades[i]  
        return itens

def adicionar_produtos():
    itens = listagem_completa()
    codigos = [i[0] for i in itens]
    produtos = [i[1] for i in itens]
    while True:
        codigo = randint(10000, 20001)
        if codigo not in codigos:
            break
        else:
            print('Código já cadastrado.')
    while True:
        produto = input('Produto a adicionar: ')
        if produto not in produtos:
            break
        else:
            print('Produto já cadastrado.')
    quantidade = input('Quantidade adicionada: ')
    dado = f'{codigo} - {produto} - Quantidade: {quantidade}\n'
    with open(pasta, 'a', encoding='UTF-8') as arquivo:
        arquivo.write(dado)
    return

def retirar_produtos():
    itens = listagem_completa()
    codigos = [i[0] for i in itens]
    frase1, frase2, frase3 = 'Código', 'Produto', 'Quantidade'
    print('Todos os produtos registrados:\n')
    print(Fore.BLUE + f'{frase1:^15} {frase2:^30} {frase3:^10}')
    for i in itens:
        print(Style.RESET_ALL + f'{i[0]:^15} {i[1]:^30} {i[2]:^10}')
    print()
    while True:
        codigo = input('Digite o código do produto a retirar: ')
        if codigo in codigos:
            for i in itens:
                if i[0] == codigo:
                    while True:
                        quantidade = int(input('Digite a quantidade a retirar: '))
                        if quantidade <= i[2]:
                            i[2] = i[2] - quantidade
                            break
                        else:
                            print('Quantidade acima do disponível.')
            break
        else:
            print('Código inexistente.')
    with open(pasta, 'w', encoding='UTF-8') as arquivo:
        for i in itens:
            arquivo.write(f'{i[0]} - {i[1]} - Quantidade: {i[2]}\n')
    return

def relatório_geral():
    itens = listagem_completa()
    print('Todos os produtos registrados:\n')
    frase1, frase2, frase3 = 'Código', 'Produto', 'Quantidade'
    print(Fore.BLUE + f'{frase1:^15} {frase2:^30} {frase3:^10}')
    for i in itens:
        print(Style.RESET_ALL + f'{i[0]:^15} {i[1]:^30} {i[2]:^10}')
    print()
    return

def produtos_indisponiveis():
    itens = listagem_completa()
    print('Produtos fora do estoque:\n')
    frase1, frase2, frase3 = 'Código', 'Produto', 'Quantidade'
    print(Fore.BLUE + f'{frase1:^15} {frase2:^30} {frase3:^10}')
    for i in itens:
        if i[2] == 0:
            print(Style.RESET_ALL + f'{i[0]:^15} {i[1]:^30} {i[2]:^10}')
    print()
    return

if __name__ == "__main__":
    print(Fore.GREEN + 'Olá! Bem-vindo ao gerenciador de estoque.')
    print(Style.RESET_ALL)
    while True:
        print('O que deseja fazer?\nA - Adicionar um produto\nB - Retirar um produto\nC - Relatório Geral\nD - Produtos Indisponíveis\nS - Sair\n')
        opcao = input('Digite A, B, C, D ou S: ')
        print()
        if opcao.upper() == 'A':
            while True:
                adicionar_produtos()
                opt = input('Adicionar outro produto? ')
                if opt not in ['Sim', 'sim', 'quero', 'Quero', 'Pode ser', 'Vamos', 'Yes']:
                    print()
                    break
        elif opcao.upper() == 'B':
            while True:
                retirar_produtos()
                opt = input('Retirar outro produto? ')
                if opt not in ['Sim', 'sim', 'quero', 'Quero', 'Pode ser', 'Vamos', 'Yes']:
                    print()
                    break
        elif opcao.upper() == 'C':
            relatório_geral()
            print()
        elif opcao.upper() == 'D':
            produtos_indisponiveis()
            print()
        elif opcao.upper() == 'S':
            print(Fore.GREEN + 'Obrigado! Volte sempre.')
            print(Style.RESET_ALL)
            break
        else:
            print(Fore.RED + 'Comando Inválido!')
            print(Style.RESET_ALL)
