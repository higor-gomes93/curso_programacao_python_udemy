'''
Faça uma função que receba um vetor de reais e retorne a média dele.
'''

def media_valores(*args):
    return sum(args)/len(args)

print(media_valores(4, 6))
