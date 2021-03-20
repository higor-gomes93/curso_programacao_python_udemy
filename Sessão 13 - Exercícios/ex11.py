'''
Faça um programa no qual o usuário informa o nome do arquivo e uma palavra,
e retorne o número de vezes que aquela palavra aparece no arquivo.
'''

raiz = 'c:/Users/Higor H/Documents/Estudos/Python'
pasta = raiz + '/Curso de Programação em Python (Udemy)/Notas de Aula/Sessão_3_Entrada.py'
palavra = input('Digite uma palavra: ')

with open(pasta, 'r', encoding='UTF-8') as arquivo:
    texto = arquivo.read()
    total = texto.count(palavra)

print(total)
