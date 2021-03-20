'''
Faça um algorítimo que calcule a média ponderada das notas de 3 provas. A primeira e a segunda prova
têm peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado
ou reprovado. A nota para aprovação deve ser igual ou superior a 60 pontos.
'''

nota_1 = int(input("Qual a nota da p1? "))
nota_2 = int(input("Qual a nota da p2? "))
nota_3 = int(input("Qual a nota da p3? "))

peso_1 = 1
peso_2 = 1
peso_3 = 2

media = ((nota_1*peso_1)+(nota_2*peso_2)+(nota_3*peso_3))/(peso_1+peso_2+peso_3)

if media >= 60:
    print(f"Aprovado com media {media}")
else:
    print(f"Reprovado com media {media}")