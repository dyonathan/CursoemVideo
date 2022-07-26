# Faz um par ou impar, só para quando jogador perder.
# Mostrar no final total de vitórias consecutivas
'''
from random import randint

vitoria = 0

while True:
    print('=-' * 15)
    print('Vamos jogar Par ou Impar!!!')
    print('=-' * 15)

    jogadorn = int(input('Vai jogar quanto: '))
    computador = randint(0, 10)
    jogadorop = 'J'

    while True:
        if jogadorop == 'P' or jogadorop == 'I':
            break
        else:
            jogadorop = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]

    total = computador + jogadorn

    if total % 2 == 0:
        print('-' * 30)
        print(f'Você jogou {jogadorn} e o computador {computador}. Total de {total} DEU PAR')
    else:
        print('-' * 30)
        print(f'Você jogou {jogadorn} e o computador {computador}. Total de {total} DEU IMPAR')

    if jogadorop[0] == 'P' and total % 2 == 0 or jogadorop[0] == 'I' and total % 2 != 0:
        print('-' * 30)
        print('Você GANHOU!!!')
        vitoria += 1
    elif jogadorop[0] == 'P' and total % 2 != 0 or jogadorop[0] == 'I' and total % 2 == 0:
        print('-' * 30)
        print('Você PERDEU!!!')
        break
    print('Vamos jogar novamente...')

print('=-' * 15)
print(f'GAME OVER! Você venceu {vitoria} vezes.')
'''

# Guanabara fez

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end=' ')
    print('Deu PAR.' if total % 2 == 0 else 'DEU IMPAR.')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
