# Ler o primeiro termo e a razão de um progressão aritmetica
'''
p = int(input('Primeiro termo da PA? '))
r = int(input('Razão da PA? '))

print('Os 10 primeiros termos dessa PA são: ')
for c in range(p, p+(r*10), r):
    print('{}'.format(c), end=' ')
'''

# Guanabara fez

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{} '.format(c), end='-> ')
print('ACABOU')
