# Faz um par ou impar, só para quando jogador perder.
# Mostrar no final total de vitórias consecutivas

from random import randint

vitoria = 0

computador = randint(0, 10)

print('=-' * 15)
print('Vamos jogar Par ou Impar!!!')

print('=-' * 15)
jogadorn = int(input('Vai jogar quanto: '))
jogadorop = str(input('Par ou Impar? [P/I]: ')).strip().upper()


total = computador + jogadorn
while True:
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
    jogadorn = int(input('Vai jogar quanto: '))
    jogadorop = str(input('Par ou Impar? [P/I]: ')).strip().upper()

print('=-' * 15)
print(f'GAME OVER! Você venceu {vitoria} vezes.')
