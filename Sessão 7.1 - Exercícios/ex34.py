'''
Faça um programa para ler 10 números DIFERENTES a serem armazenados em um vetor. Os dados deverão ser armazenados
no vetor na ordem que forem sendo lidos, sendo que caso o usuário digite um número que já foi digitado anteriormente,
o programa deverá pedir para ele digitar outro número. Note que cada valor digitado pelo usuário deve ser pesquisado
no vetor, verificando se ele existe entre os números que já foram fornecidos. Exibir na tela o vetor final que foi
digitado.
'''

vetor = []

while len(vetor) < 10:
    num = int(input(f'Digite o {len(vetor)+1}º número do vetor: '))
    if num not in vetor:
        vetor.append(num)

print(f'O vetor digitado foi {vetor}.')
