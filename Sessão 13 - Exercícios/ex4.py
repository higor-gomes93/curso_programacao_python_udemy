'''
Faça um programa que receba do usuário um arquivo de texto e mostre na tela quantas letras são vogais e quantas são consoantes.
'''

raiz = 'c:/Users/Higor H/Documents/Estudos/Python'
pasta = raiz + '/Curso de Programação em Python (Udemy)/Notas de Aula/Sessão_3_Entrada.py'
vogais = ['a', 'e', 'i', 'o', 'u']
vogais.extend([i.upper() for i in vogais])
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
consoantes.extend([i.upper() for i in consoantes])

with open(pasta, 'r', encoding='UTF-8') as arquivo:
    vog = 0
    cons = 0
    for i in arquivo.read():
        if i in vogais:
            vog += 1
        elif i in consoantes:
            cons += 1

print(f'Existem {vog} vogais e {cons} consoantes no texto.')
