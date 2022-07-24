# Computador vai escolher um número de 0 a 10 e você vai tentar adivinhar o número
'''
from random import randint

cont = 1
computador = randint(0, 10)
print('O computador escolheu um número de 0 a 10, tente adivinhar!')
jogador = int(input('Qual foi? '))
while computador != jogador:
    print('Você errou, tente novamente!')
    cont += 1
    jogador = int(input('Qual número? '))

print('Parabéns eu pensei no {}, e você acertou em {} tentativa(s)!'.format(computador, cont))
'''

# guanabara fez

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        else:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
