# Jogo de jokenpô (pedra, papel ou tesoura)

from random import randint
import emoji

j = int(input('''Jogo pedra, papel e tesoura
1 - Pedra \u270A\uFE0F
2 - Papel \U0001f91a\uFE0F
3 - Tesoura \u270C\uFE0F
Vai jogar oque: '''))

pc = randint(1, 3)

if j == 1 and pc == 3 or j == 2 and pc == 1 or j == 3 and pc == 2:
    print('Você ganhou!')
elif j == 1 and pc == 2 or j == 2 and pc == 3 or j == 3 and pc == 1:
    print('Você perdeu!')
elif j == 1 and pc == 1 or j == 2 and pc == 2 or j == 3 and pc == 3:
    print('Empate!')
else:
    print('Opção invalida!')
