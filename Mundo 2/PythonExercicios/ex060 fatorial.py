# Programa que lê um número e mostra o seu fatorial
'''
fatorial = 1

n = int(input('Qual número você quer fazer o fatorial: '))

# com for
for c in range(n, 1, -1):
    fatorial = fatorial * c

# com while
c = n
while c > 0:
    fatorial = fatorial * c
    c = c - 1

print('{}!(fatorial) da {}!'.format(n, fatorial))
'''

# Guanabara fez

# usando a biblioteca math
'''
from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))
'''

# usando o while

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
