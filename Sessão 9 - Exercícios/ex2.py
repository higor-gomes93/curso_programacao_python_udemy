'''
Faça programas para calcular as seguintes sequências:
a) 1 + 2 + 3 + 4 + 5 + ... + n
b) 1 - 2 + 3 - 4 + 5 + ... + (2n-1)
c) 1 + 3 + 5 + 7 + ... + (2n-1)
'''

num = int(input('Digite um número n: '))

seq1 = [x for x in range(1, num+1)]
seq2 = [x if x%2 != 0 else -x for x in range(1, 2*num)]
seq3 = [x for x in range(1, num*2) if x%2 != 0]

print(sum(seq1))
print(sum(seq2))
print(sum(seq3))

# Modo chique -> x%2: se x for par, isso vale 0, e 0 = False; se x for ímpar, isso vale 1, e 1 = True
seq1 = [x for x in range(1, num+1)]
seq2 = [x if x%2 else -x for x in range(1, 2*num)]
seq3 = [x for x in range(1, num*2) if x%2]

print(sum(seq1))
print(sum(seq2))
print(sum(seq3))
