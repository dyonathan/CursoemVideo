#Pergunta quantos jogos a pessoa quer fazer
#Gerar altomaticamente os jogos (sortear 6 números de 1 a 60 em ordem crescente)

from random import randint
from time import sleep

jogos = []
qtd = []

print('-=' * 15)
print(f'{"MEGA SENA":^30}')
print('-=' * 15)

qtd = int(input(f'Quantos jogos serão feitos: '))
for c in range(0, qtd):
    jogos[c] = ' '


print(qtd)
print(jogos)
