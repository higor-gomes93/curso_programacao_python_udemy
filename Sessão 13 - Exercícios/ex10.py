'''
Faça um programa que receba o nome de um arquivo de entrada e outro de saída. O
arquivo de entrada contém em cada linha o nome de uma cidade e seu número de habitantes.
O programa deverá ler o arquivo de entrada e gerar um arquivo de saída onde aparece
o nome da cidade mais populosa seguida pelo seu número de habitantes.
'''

raiz = 'c:/Users/Higor H/Documents/Estudos/Python/Curso de Programação em Python (Udemy)'
pasta1 = raiz + '/Sessão 13 - Exercícios/ex10_1.txt'
pasta2 = raiz + '/Sessão 13 - Exercícios/ex10_2.txt'

def substituir(texto):
    novo_texto = ""
    vetor = []
    for caracter in texto:
        if caracter < " ":
            vetor.append("/")
        else:
            vetor.append(caracter)
    texto_final = novo_texto.join(vetor)
    return texto_final

with open(pasta1, 'r', encoding='UTF-8') as arquivo1:
    catalogo = {}
    while True:
        linha = arquivo1.readline()
        if linha > " ":
            item = substituir(linha).split('/')
            catalogo[item[2]] = int(item[3].replace(".",""))
        else:
            break

with open(pasta2, 'w', encoding='UTF-8') as arquivo2:
    maior = [i for i in catalogo.items() if i[1] == max(catalogo.values())]
    cidade = maior[0][0]
    habitantes = "{:,}".format(maior[0][1]).replace(",",".")
    arquivo2.write(f'A cidade mais povoada é {cidade}, com {habitantes} habitantes.')
