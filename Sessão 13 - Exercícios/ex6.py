'''
Faça um programa que receba do usuário um arquivo de texto e mostre na tela quantas vezes cada letra do alfabeto aparece dentro do arquivo.
'''

from collections import Counter

raiz = 'c:/Users/Higor H/Documents/Estudos/Python'
pasta = raiz + '/Curso de Programação em Python (Udemy)/Notas de Aula/Sessão_3_Entrada.py'

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

with open(pasta, 'r', encoding='UTF-8') as arquivo:
    letras = filter(lambda x: x in alfabeto, arquivo.read().lower())

print(Counter(letras))
