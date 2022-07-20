# Ver se um número é primo
'''
# inicializa a variável s
s = 0
n = int(input('Digite um número: '))

# coloca n + 1 porque ele conta somente até o número antes de n
for c in range(1, n + 1):
    if n % c == 0:
        s += 1
# 2 porque tem que dividir por 1 e ele mesmo
if s != 2:
    print('Não é um número primo!')
else:
    print('É um número primo!')
'''

# Guanabara fez

num = int(input('Digite um número: '))
tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[31m', end='')
        tot += 1
    else:
        print('\033[m', end='')
    print('{} '.format(c), end='')

print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))

if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
