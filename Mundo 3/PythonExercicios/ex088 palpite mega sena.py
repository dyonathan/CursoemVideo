#Pergunta quantos jogos a pessoa quer fazer
#Gerar altomaticamente os jogos (sortear 6 números de 1 a 60 em ordem crescente)
'''
from random import randint
from time import sleep

jogos = []

print('-=' * 15)
print(f'{"MEGA SENA":^30}')
print('-=' * 15)

qtd = int(input(f'Quantos jogos serão feitos: '))
print(f'-=-=-=-= SORTEANDO {qtd} JOGOS -=-=-=-=')
for c in range(0, qtd):
    while True:
        jogo = randint(1, 60)
        if jogo not in jogos:
            jogos.append(jogo)
            if len(jogos) == 6:
                break
    jogos.sort()
    print(f'O jogo {c + 1} é: {jogos}')
    sleep(1)
    jogos.clear()
print('-=-=-=-=-= < BOA SORTE > -=-=-=-=-=')
'''
#Guanabara fez

from random import randint
from time import sleep
lista = list()
jogos = list()
print('-=' * 30)
print('       JOGA NA MEGA SENA')
print('-=' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
