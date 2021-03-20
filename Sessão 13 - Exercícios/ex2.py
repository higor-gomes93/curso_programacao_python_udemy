'''
Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas linhas esse arquivo
possui.
'''

raiz = 'c:/Users/Higor H/Documents/Estudos/Python/'
caminho = raiz + 'Curso de Programação em Python (Udemy)/Notas de Aula/Sessão_6_Loops.py'

with open(caminho, 'r', encoding='UTF-8') as arquivo:
    print(len(arquivo.readlines()))
