#Fazer uma função chamada maior()
#Ler n valores
#Falar qual é o maior
from time import sleep


def separador():
    print('-=' * 30)
    print('Analisando os valores passados...')


def valores(* num):
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.3)
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {max(num)}.')


separador()
valores(2, 9, 4, 5, 7, 1)
separador()
valores(4, 7, 0)
separador()
valores(1, 2)
separador()
valores(6)
separador()
valores(0)
