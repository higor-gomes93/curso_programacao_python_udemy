'''
Faça um programa que calcule a diferença entre a soma dos quadrados dos primeiros 100 números naturais
e o quadrado da soma.
'''

somaquadrados = sum(map(lambda x: x**2, range(1, 101)))
quadradosoma = sum(range(1, 101))**2
print(abs(somaquadrados-quadradosoma))
