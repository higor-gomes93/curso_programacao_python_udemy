'''
Faça um programa que calcule o menor número divisível por cada um dos números de 1 a 20.
'''
inicio = 1
fim = 20   # Substituir por 20. No enunciado, ele fala que pra 10, retorna 2520.
valor = 1
num = fim  
cont = 0

while valor == 1:    
    for i in range(inicio, fim+1):  
        if num%i != 0:
            cont = cont + 1
    if cont != 0:    
        num = num + 1
        cont = 0
    else:
        valor = num

print(valor)
