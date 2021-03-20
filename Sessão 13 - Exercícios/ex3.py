'''
Faça um programa que receba do usuário um arquivo de texto e mostre na tela quantas letras são vogais.
'''

raiz = 'c:/Users/Higor H/Documents/Estudos/Python'
pasta = raiz + '/Curso de Programação em Python (Udemy)/Notas de Aula/Sessão_3_Entrada.py'
vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

with open(pasta, 'r', encoding='UTF-8') as arquivo:
    cont = 0
    for i in arquivo.read():
        if i in vogais:
            cont += 1

print(f'Existem {cont} vogais no texto.')
