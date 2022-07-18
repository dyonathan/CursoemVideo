# Jogo de jokenpô (pedra, papel ou tesoura)
'''
from random import randint
import emoji

j = int(input(''''''Jogo pedra, papel e tesoura
1 - Pedra \u270A\uFE0F
2 - Papel \U0001f91a\uFE0F
3 - Tesoura \u270C\uFE0F
Vai jogar oque: ''''''))

pc = randint(1, 3)

if j == 1 and pc == 3 or j == 2 and pc == 1 or j == 3 and pc == 2:
    print('Você ganhou!')
elif j == 1 and pc == 2 or j == 2 and pc == 3 or j == 3 and pc == 1:
    print('Você perdeu!')
elif j == 1 and pc == 1 or j == 2 and pc == 2 or j == 3 and pc == 3:
    print('Empate!')
else:
    print('Opção invalida!')
'''

# Guanabara fez mais completo

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
if computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
if computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')

