# Ler número inteiro e mostrar n primeiros elementos da sequência de fibonacci
# ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8 -> 13 -> 21...

print('-' * 30)
print('Sequência de Fibonacci!')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 30)
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
print('~' * 30)
