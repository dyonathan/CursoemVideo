#Fazer um contador com a função contador()
#Ler três parametros: inicio, fim e passo e fazer três contagens
#Mostrar:
#a)De 1 até 10, de 1 em 1
#b)De 10 até 0, de 2 em 2
#c)Uma contagem personalizada
'''
from time import sleep


def separador():
    print('-=' * 20)


def timer():
    sleep(0.3)


def contador():
    separador()
    print('Contagem de 1 até 10 de 1 em 1')
    for c in range(1, 11, 1):
        print(c, end=' ')
        timer()
    print('FIM!')

    separador()
    print('Contagem de 10 até 0 de 2 em 2')
    for c in range(10, -1, -2):
        print(c, end=' ')
        timer()
    print('FIM!')

    separador()
    inicio = int(input(f'{"Início:":<8}'))
    fim = int(input(f'{"Fim:":<8}'))
    passo = int(input(f'{"Passo:":<8}'))
    if passo < 0:
        passo *= (-1)
    elif passo == 0:
        passo = 1
    separador()
    if inicio < fim:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for c in range(inicio, fim+1, passo):
            print(c, end=' ')
            timer()
    elif inicio > fim:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for c in range(inicio, fim-1, -passo):
            print(c, end=' ')
            timer()
    print('FIM!')


contador()
'''

#Guanabara fez

from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM!')


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
