'''
Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado, uma sequência
arbitrária de notas (válidas no intervalo de 10 a 20) e que mostre na tela, como resultado, a
correspondente média aritmética. O número de notas com que o aluno pretende efetuar o cálculo não
será fornecido ao programa, o qual terminará quando for introduzido um valor que não seja válido
como nota de aprovação.
'''

input("Olá! Irei calcular a média das notas digitadas. Elas deverão estar no intervalo especificado.")
input("Digite um valor fora do intervalo para parar o programa.")

cont = 0
soma = 0

while True:
    nota = float(input("Digite uma nota entre 10 e 20: "))
    if nota >= 10 and nota <= 20:
        soma += nota
        cont += 1
    else:
        break

if cont != 0:
    media = soma/cont
else:
    media = 0

print(f"A média das notas é {media}.")
