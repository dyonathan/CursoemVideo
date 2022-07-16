# Se menor de 18 ainda vai se alistar, se 18 está na hora e se mais passou

from datetime import date

nas = int(input('Em qual ano você nasceu? '))
ano = date.today().year
idade = ano - nas

if idade < 18:
    print('Ainda faltam {} anos para o alistamento!'.format(18 - idade))
elif idade == 18:
    print('Está na hora de se alistar!')
else:
    print('Já passou {} anos do alistamento!'.format(idade - 18))
