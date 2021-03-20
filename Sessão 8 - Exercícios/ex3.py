'''
Faça uma função para verificar se um número é positivo ou negativo. Sendo que o valor de retorno será 1 se positivo,
-1 se negativo e 0 se for igual a 0.
'''

def number_check(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    return 0

print(number_check(3))
print(number_check(-5))
print(number_check(0))
