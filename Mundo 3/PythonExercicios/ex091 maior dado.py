#Ler 4 dados guardar em um dicionario, mostrar em ordem e falar qual o maior
from random import randint
from time import sleep

pos = 1

dado = [randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)]
jogadores = {'jogador1': dado[0], 'jogador2': dado[1], 'jogador3': dado[2], 'jogador4': dado[3]}

print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'   O {k} tirou {v}')
    sleep(1)

print('Ranking dos jogadores:')
for k in sorted(jogadores, key=jogadores.get, reverse=True):
    print(f'   {pos}º lugar: {k} com {jogadores[k]}')
    sleep(1)
    pos += 1
