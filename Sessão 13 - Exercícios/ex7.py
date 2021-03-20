'''
Faça um programa que receba do usuário um arquivo texto. Crie outro arquivo texto contendo
o texto do arquivo de entrada, mas com as vogais substituídas por '*'.
'''

raiz = 'c:/Users/Higor H/Documents/Estudos/Python/Curso de Programação em Python (Udemy)'
pasta = raiz + '/Notas de Aula/Sessão_3_Entrada.py'

vogais = ['a', 'e', 'i', 'o', 'u']
vogais.extend([i.upper() for i in vogais])

with open(pasta, 'r', encoding='UTF-8') as arquivo1:
    texto = arquivo1.read()

with open(raiz + '/Sessão 13 - Exercícios/ex7.txt', 'w', encoding='UTF-8') as arquivo2:
    for caracter in texto:
        if caracter in vogais:
            arquivo2.write('*')
        else:
            arquivo2.write(caracter)
