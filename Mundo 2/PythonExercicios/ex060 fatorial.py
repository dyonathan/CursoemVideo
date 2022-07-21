# Programa que lê um número e mostra o seu fatorial

fatorial = 1

n = int(input('Qual número você quer fazer o fatorial: '))

for c in range(n, 1, -1):
    fatorial = fatorial * c

print('{}!(fatorial) da {}!'.format(n,fatorial))
