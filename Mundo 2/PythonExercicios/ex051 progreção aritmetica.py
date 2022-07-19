# Ler o primeiro termo e a razão de um progressão aritmetica

p = int(input('A progressão começa em qual número? '))
r = int(input('Somar de quanto em quanto? '))

print('Os 10 primeiros termos dessa PA são: ')
for c in range(p, p+(r*10), r):
    print('{}'.format(c))
