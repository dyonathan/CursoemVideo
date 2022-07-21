# Computador vai escolher um número de 0 a 10 e você vai tentar adivinhar o número

from random import randint

cont = 0
computador = randint(0, 10)
print('O computador escolheu um número de 0 a 10, tente adivinhar!')
jogador = int(input('Qual foi? '))
while computador != jogador:
    print('Você errou, tente novamente!')
    cont += 1
    jogador = int(input('Qual número? '))

print('Parabéns eu pensei no {}, e você acertou em {} tentativa(s)!'.format(computador, cont))
