'''
Implemente uma função a qual recebe duas strings, str1 e str2, e um valor inteiro positivo N. A função concatena
não mais que N caracteres da string str2 à string str1.
'''

def concatena_parcial(str1, str2, ene):
    str3 = str1 + str2[:ene+1]
    return str3

print(concatena_parcial('Boa ', 'tardes', 5))
print(concatena_parcial('Boa ', 'tardes', 4))
print(concatena_parcial('Boa ', 'tardes', 3))
