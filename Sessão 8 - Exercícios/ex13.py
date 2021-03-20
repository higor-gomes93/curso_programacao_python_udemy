'''
Faça uma função que receba dois valores numéricos e um símbolo. Este símbolo representará a operação que deseja
efetuar com os números. Símbolos: +, -, * e /.
'''

def conta(num1, num2, simbolo):
    if simbolo == '+':
        return num1+num2
    elif simbolo == '-':
        return num1-num2
    elif simbolo == '*':
        return num1*num2
    elif simbolo == '/':
        return num1/num2
    return 'Símbolo inválido.'

print(conta(8, 2, '+'))
print(conta(8, 2, '-'))
print(conta(8, 2, '*'))
print(conta(8, 2, '/'))
