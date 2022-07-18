# Se menor de 18 ainda vai se alistar, se 18 está na hora e se mais passou
'''
from datetime import date

nas = int(input('Em qual ano você nasceu? '))
ano = date.today().year
idade = ano - nas

print('Quem nasceu em {} tem {} anos em {}.'.format(nas, idade, date.today().year))

if idade < 18:
    print('Ainda faltam {} anos para o alistamento!'.format(18 - idade))
    print('Seu alistamento será em {}.'.format(nas + 18))
elif idade == 18:
    print('Está na hora de se alistar!')
else:
    print('Já passou {} anos do alistamento!'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(nas + 18))
'''

# Guanabara fez

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
else:
    saldo = 18 - idade
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento foi em {}.'.format(ano))
