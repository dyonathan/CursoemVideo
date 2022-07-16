# Ler ano do nascimento, se até 9 anos mirim,até 14 infantil, ate 19 junior, ate 20 senior se acima master

from datetime import date

nasc = int(input('Em que ano você nasceu? '))

idade = date.today().year - nasc
print('Você tem {} anos, sua categoria é: '.format(idade))
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 20:
    print('Sênior')
else:
    print('Master')
