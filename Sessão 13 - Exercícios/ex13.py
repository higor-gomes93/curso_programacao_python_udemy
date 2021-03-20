'''
Faça um programa que permita que o usuário entre com diversos nomes e telefone para
cadastro, e crie um arquivo com essas informações, uma por linha. O usuário finaliza
a entrada com '0' para o telefone.
'''

raiz = 'c:/Users/Higor H/Documents/Estudos/Python'
pasta = raiz + '/Curso de Programação em Python (Udemy)/Sessão 13 - Exercícios/ex13.txt'

with open(pasta, 'w', encoding='UTF-8') as arquivo:
    while True:
        nome = input('Digite o nome do contato: ')
        numero = input('Digite o número do contato: ')
        if numero != '0':
            arquivo.write(f'{nome}: {numero}\n')
        else:
            break
