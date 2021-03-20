'''
Faça uma função que receba dois números e retorne qual deles é o maior.
'''

def comparador(num1, num2):
    if num1 > num2:
        return f'O número {num1} é maior que o número {num2}.'
    elif num1 < num2:
        return f'O número {num2} é maior que o número {num1}.'
    return f'O número {num1} é igual ao número {num2}.'

print(comparador(3, 5))
print(comparador(7, 5))
print(comparador(3, 3))
