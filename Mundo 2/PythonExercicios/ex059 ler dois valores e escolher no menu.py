'''
ler dois valores e mostrar um menu
[ 1 ]somar
[ 2 ]multiplicar
[ 3 ]maior
[ 4 ]novos números
[ 5 ]sair do programa
'''

from time import sleep

op = 0

n1 = float(input('Qual o primeiro número? '))
n2 = float(input('Qual o segundo número? '))

while op != 5:

    op = int(input('''Oque deseja fazer?
[ 1 ]Somar
[ 2 ]Multiplicar
[ 3 ]Maior
[ 4 ]Novos números
[ 5 ]Sair do programa
Qual a opção escolhida: '''))

    if op == 1:
        print('A soma de {} e {} é {}!!!'.format(n1, n2, n1 + n2))
        sleep(3)
    if op == 2:
        print('A multiplicação de {} por {} é {}!!!'.format(n1, n2, n1 * n2))
        sleep(3)
    if op == 3:
        if n1 > n2:
            print('O {} é maior que o {}!'.format(n1, n2))
            sleep(3)
        else:
            print('O {} é maior que o {}!'.format(n2, n1))
            sleep(3)
    if op == 4:
        n1 = float(input('Qual o novo primeiro número? '))
        n2 = float(input('Qual o novo segundo número? '))

print('Até mais!!!')
sleep(2)
