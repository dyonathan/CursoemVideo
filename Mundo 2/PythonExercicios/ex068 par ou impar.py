# Faz um par ou impar, só para quando jogador perder.
# Mostrar no final total de vitórias consecutivas

from random import randint

op = ['Par', 'Impar']
vitoria = 0

computador = randint(0, 10)

print('Vamos jogar Par ou Impar!!!')

jogadorn = int(input('Vai jogar quanto: '))
jogadorop = str(input('Par ou Impar? [P/I]: ')).strip().upper()

total = computador + jogadorn

#if jogadorop[0] == 'I' and total % 2 != 0:
print(f'Você jogou {jogadorn} e o computador {computador}. Total de {total} DEU' if total % 2 == 0 'PAR' else 'IMPAR')

'''elif jogadorop[0] == 'P' and total % 2 == 0:
    print(f'Você jogou {jogadorn} e o computador {computador}. Total de {total} DEU PAR')

elif jogadorop[0] == 'P' and total % 2 != 0:
    print(f'Você jogou {jogadorn} e o computador {computador}. Total de {total} DEU PAR')'''


