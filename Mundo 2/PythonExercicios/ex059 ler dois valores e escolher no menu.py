'''
ler dois valores e mostrar um menu
[ 1 ]somar
[ 2 ]multiplicar
[ 3 ]maior
[ 4 ]novos números
[ 5 ]sair do programa
'''
'''
from time import sleep

op = 0

n1 = float(input('Qual o primeiro número? '))
n2 = float(input('Qual o segundo número? '))

while op != 5:

    op = int(input(Oque deseja fazer?
[ 1 ]Somar
[ 2 ]Multiplicar
[ 3 ]Maior
[ 4 ]Novos números
[ 5 ]Sair do programa
Qual a opção escolhida: ))

    if op == 1:
        print('A soma de {} e {} é {}!!!'.format(n1, n2, n1 + n2))
    elif op == 2:
        print('A multiplicação de {} por {} é {}!!!'.format(n1, n2, n1 * n2))
    elif op == 3:
        if n1 > n2:
            print('O {} é maior que o {}!'.format(n1, n2))
        else:
            print('O {} é maior que o {}!'.format(n2, n1))
    elif op == 4:
        n1 = float(input('Qual o novo primeiro número? '))
        n2 = float(input('Qual o novo segundo número? '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Opção Inválida! Tente novamente!')

    sleep(2)

print('Até mais!!!')
sleep(1)
'''

# Guanabara fez

from time import  sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''       [ 1 ] Somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('>>>>> Qual é a sua opçao? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente!')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')
