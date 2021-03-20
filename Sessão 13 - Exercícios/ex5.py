'''
Faça um programa que receba do usuário um arquivo texto e um caracter. Mostre na tela quantas vezes aquele caracter ocorre dentro do arquivo.
'''

raiz = 'c:/Users/Higor H/Documents/Estudos/Python'
pasta = raiz + '/Curso de Programação em Python (Udemy)/Notas de Aula/Sessão_3_Entrada.py'

while True:
    caracter = input('Digite um caracter: ')
    if len(caracter) > 1:
        print('Erro: A entrada precisa ser apenas 1 caracter.')
    else:
        break


with open(pasta, 'r', encoding='UTF-8') as arquivo:
    cont = 0
    for i in arquivo.read():
        if i == caracter:
            cont += 1

print(f'O caracter "{caracter}" aparece {cont} vezes no texto.')
