#Ler 4 dados guardar em um dicionario, mostrar em ordem e falar qual o maior
from random import randint

jogadores = dict()
dado = list()
ordem = list()

'''
for c in range(0, 4):
    jogadores['dado'] = randint(1, 7)
    dado.append(jogadores.copy())

ordem.append()
#dado.sort()
print(dado)
'''
j = list()
d = list()

for c in range(1, 5):
    j = randint(0, 7)
    print(f'O jogador{c} tirou {j}')
    d.append(j[:])

d.sort()
print('Ranking dos jogadores: ')
for c, v in enumerate(d):
    print(f'{c}º lugar: jogador{v} com')

