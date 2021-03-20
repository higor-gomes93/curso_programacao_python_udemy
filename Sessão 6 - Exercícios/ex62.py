'''
Se os números de 1 a 5 são escritos em palavras: um, dois, três, quatro, cinco, então 
há 2 + 4 + 4 + 6 + 5 = 22 letras usadas no total. Faça um programa que conte quantas letras
seriam utilizadas se todos os números de 1 a 1000 fossem escritos em palavras. Obs.: não conte
espaços ou hifens.
'''

import inflect

p = inflect.engine()

var = p.number_to_words(4)
total = len(var)

print(total)

print(var)

