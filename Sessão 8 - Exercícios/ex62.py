'''
Crie uma função que calcula o comprimento de uma string. 
'''

def tamanho_string(string):
    cont = 0
    for i in string:
        cont += 1
    return cont

print(tamanho_string('Boa tarde'))
print(len('Boa tarde'))
