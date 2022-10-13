#Pergunta quantos jogos a pessoa quer fazer
#Gerar altomaticamente os jogos (sortear 6 números de 1 a 60 em ordem crescente)

from random import randint
from time import sleep

jogos = []
temp = []

print('-=' * 15)
print(f'{"MEGA SENA":^30}')
print('-=' * 15)

qtd = int(input(f'Quantos jogos serão feitos: '))
for v in range(0, qtd):
    print(f'O jogo é: ', end='')
    for c in range(0, 6):
        temp.append(randint(0, 60))
        if jogos not in temp:
            jogos.append(temp[:])
            if len(jogos) == 6:
                jogos.sort()
                print(jogos, end=' ')
            temp.clear()
    jogos.clear()
    print()
