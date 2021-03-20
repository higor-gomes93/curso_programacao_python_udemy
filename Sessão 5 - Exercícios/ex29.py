'''
Faça uma prova de matemática para crianças que estão aprendendo a somar números inteiros menores 
que 100. Escolha número aleatórios entre 1 e 100, e mostre na tela a pergunta: qual é a soma
de a + b, onde a e b são os números aleatórios. Peça a resposta. Faça cinco perguntas ao aluno,
e mostre para ele as perguntas e as respostas corretas, além de quantas vezes o aluno acertou.
'''

# Entrada
print("Ola! Bem-vindo ao teste de matematica. Você precisara responder a 5 perguntas.")

# Aquisição das perguntas
print("Pergunta 1")
a_1 = int(input("Digite um numero inteiro entre 1 e 100: "))
b_1 = int(input("Agora, digite outro numero inteiro entre 1 e 100: "))
resp_1 = int(input(f"Qual o resultado da soma {a_1} + {b_1}? "))

print("Pergunta 2")
a_2 = int(input("Digite um numero inteiro entre 1 e 100: "))
b_2 = int(input("Agora, digite outro numero inteiro entre 1 e 100: "))
resp_2 = int(input(f"Qual o resultado da soma {a_2} + {b_2}? "))

print("Pergunta 3")
a_3 = int(input("Digite um numero inteiro entre 1 e 100: "))
b_3 = int(input("Agora, digite outro numero inteiro entre 1 e 100: "))
resp_3 = int(input(f"Qual o resultado da soma {a_3} + {b_3}? "))

print("Pergunta 4")
a_4 = int(input("Digite um numero inteiro entre 1 e 100: "))
b_4 = int(input("Agora, digite outro numero inteiro entre 1 e 100: "))
resp_4 = int(input(f"Qual o resultado da soma {a_4} + {b_4}? "))

print("Pergunta 5")
a_5 = int(input("Digite um numero inteiro entre 1 e 100: "))
b_5 = int(input("Agora, digite outro numero inteiro entre 1 e 100: "))
resp_5 = int(input(f"Qual o resultado da soma {a_5} + {b_5}? "))

# Respostas corretas
print("Aqui vai o gabarito do questionario!")
print(f"Q1 - Qual o resultado da soma {a_1} + {b_1}? \nSua resposta: {resp_1} \nResposta correta: {a_1 + b_1}")
print(f"Q2 - Qual o resultado da soma {a_2} + {b_2}? \nSua resposta: {resp_2} \nResposta correta: {a_2 + b_2}")
print(f"Q3 - Qual o resultado da soma {a_3} + {b_3}? \nSua resposta: {resp_3} \nResposta correta: {a_3 + b_3}")
print(f"Q4 - Qual o resultado da soma {a_4} + {b_4}? \nSua resposta: {resp_4} \nResposta correta: {a_4 + b_4}")
print(f"Q5 - Qual o resultado da soma {a_5} + {b_5}? \nSua resposta: {resp_5} \nResposta correta: {a_5 + b_5}")

# Cálculo da pontuação
if resp_1 == a_1 + b_1:
    cont_1 = 1
else:
    cont_1 = 0
if resp_2 == a_2 + b_2:
    cont_2 = 1
else:
    cont_2 = 0
if resp_3 == a_3 + b_3:
    cont_3 = 1
else:
    cont_3 = 0
if resp_4 == a_4 + b_4:
    cont_4 = 1
else:
    cont_4 = 0
if resp_5 == a_5 + b_5:
    cont_5 = 1
else:
    cont_5 = 0

resultado = cont_1 + cont_2 + cont_3 + cont_4 + cont_5
print(f"Das 5 perguntas, voce acertou {resultado}!")
