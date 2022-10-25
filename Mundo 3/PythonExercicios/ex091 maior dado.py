#Ler 4 dados guardar em um dicionario, mostrar em ordem e falar qual o maior
'''
from random import randint
from time import sleep

pos = 1

jogadores = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}

print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'   O {k} tirou {v}')
    sleep(1)

print('Ranking dos jogadores:')
for k in sorted(jogadores, key=jogadores.get, reverse=True):
    print(f'   {pos}º lugar: {k} com {jogadores[k]}')
    sleep(1)
    pos += 1
'''
#Guanabara Fez

from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print(' == RANKING DOS JOGADORES == ')
for i, v in enumerate(ranking):
    print(f'   {i + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)

