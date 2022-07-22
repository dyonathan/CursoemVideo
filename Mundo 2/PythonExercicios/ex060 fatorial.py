# Programa que lê um número e mostra o seu fatorial

fatorial = 1

n = int(input('Qual número você quer fazer o fatorial: '))

''' com for
for c in range(n, 1, -1):
    fatorial = fatorial * c
'''

# com while
c = n
while c > 0:
    fatorial = fatorial * c
    c = c - 1

print('{}!(fatorial) da {}!'.format(n, fatorial))

