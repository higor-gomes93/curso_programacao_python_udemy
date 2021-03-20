'''
Faça um programa que receba dois arquivos do usuário, e crie um terceiro arquivo com o
conteúdo dos dois primeiros juntos (o conteúdo do primeiro seguido do conteúdo do 
segundo).
'''

raiz = 'c:/Users/Higor H/Documents/Estudos/Python/Curso de Programação em Python (Udemy)'
pasta1 = raiz + '/Notas de Aula/Sessão_3_Entrada.py'
pasta2 = raiz + '/Notas de Aula/Sessão_4_TiposdeDados.py'
pasta3 = raiz + '/Sessão 13 - Exercícios/ex9.txt'

with open(pasta1, 'r', encoding='UTF-8') as arquivo1:
    texto1 = arquivo1.read()

with open(pasta2, 'r', encoding='UTF-8') as arquivo2:
    texto2 = arquivo2.read()

with open(pasta3, 'w', encoding='UTF-8') as arquivo3:
    arquivo3.write(texto1)
    arquivo3.write(texto2)
