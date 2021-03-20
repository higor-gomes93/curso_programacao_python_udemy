'''
Faça uma função que receba dois números inteiros positivos por parâmetro e retorne a soma dos N números
inteiros existentes entre eles.
'''

def soma_numeros(num1, num2):
    soma = 0
    for i in range(num1+1, num2):
        soma += i
    return soma

print(soma_numeros(2, 10))
print(soma_numeros(2, 1000))
