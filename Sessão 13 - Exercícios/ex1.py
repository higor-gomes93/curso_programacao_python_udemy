'''
Escreva um programa que:
    a) Crie/abra um arquivo texto de nome arq.txt
    b) Permita que o usuário grave diversos caracteres nesse arquivo, até que o usuário entre
    com o caractere 0
    c) Feche o arquivo
Agora, leia o arquivo, caractere por caractere, e escreva na tela todos os caracteres armazenados.
'''

# Primeira Maneira
raiz = 'c:/Users/Higor H/Documents/Estudos/Python/'
caminho = raiz + 'Curso de Programação em Python (Udemy)/Sessão 13 - Exercícios/'
nome = caminho + 'ex1.txt'

# Criando e abrindo o caminho
arquivo = open(nome, 'w', encoding='UTF-8')

# Escrevendo
while True:
    num = int(input('Digite um número: '))
    if num != 0:
        arquivo.write(str(num))
    else:
        break

# Lendo
arquivo = open(nome, 'r', encoding='UTF-8')
print(arquivo.read())

# Fechando o arquivo
arquivo.close()


# Segunda Maneira
# Criando e abrindo
with open(nome, 'w', encoding='UTF-8') as arquivo:
    while True:
        num = int(input('Digite um número: '))
        if num != 0:
            arquivo.write(str(num))
        else:
            break

# Lendo
with open(nome, 'r', encoding='UTF-8') as arquivo:
    print(arquivo.read())
