'''
Crie uma função que compara duas strings e que retorna se elas são iguais ou diferentes. 
'''

def compara_string(string1, string2):
    if string1 == string2:
        return 'São iguais.'
    return 'São diferentes.'

print(compara_string('Alo', 'Alo'))
print((compara_string('Alo', 'Hello')))
