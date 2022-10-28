#Fazer um contador com a função contador()
#Ler três parametros: inicio, fim e passo e fazer três contagens
#Mostrar:
#a)De 1 até 10, de 1 em 1
#b)De 10 até 0, de 2 em 2
#c)Uma contagem personalizada
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
