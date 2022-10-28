#Fazer duas funções sorteia() e somaPar()
#A primeira sorteia 5 números e coloca em uma lista
#A segunda mostra a soma entre todos os valores pares
from random import randint
from time import sleep
numeros = list()
temp = list()


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        temp = randint(0, 10)
        numeros.append(temp)
        print(temp, end=' ')
        sleep(0.3)
    print('PRONTO!')


def somaPar():
    print(f'Somando os valores pares de {numeros}, temos {sum(numeros)}')


sorteia()
somaPar()
