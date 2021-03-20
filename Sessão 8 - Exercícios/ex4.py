'''
Faça uma função para verificar se um número é um quadrado perfeito. Um quadrado perfeito é um número inteiro não
negativo que pode ser expresso como o quadrado de outro número inteiro.
'''

def check_square(number):
    if number**0.5 == int(number**0.5):
        return f'O número {number} é um quadrado perfeito.'
    return f'O número {number} não é um quadrado perfeito.'

print(check_square(2))
print(check_square(16))
print(check_square(27))
print(check_square(0))
