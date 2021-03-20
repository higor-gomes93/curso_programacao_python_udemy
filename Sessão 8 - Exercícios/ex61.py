'''
Escreva uma função que compare e retorne verdadeiro, caso uma string seja anagrama da outra, e falso, caso contrário.
'''

def comparar(string1, string2):
    if string1 == string2[::-1]:
        return 'Verdadeiro'
    return 'Falso'

print(comparar('arara', 'arara'))
print(comparar('arara', 'pomba'))
