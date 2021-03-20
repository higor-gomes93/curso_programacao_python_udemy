'''
Faça um programa que calcule o menor número divisível por cada um dos números de 1 a 20.
'''

num = 20

lista = [i for i in range(1, num+1)]

i = 1
while any(map(lambda x: i%x, lista)) == True:
    i += 1

print(i)
