# ler e falar o tipo primitivo e todas as infomações possiveis

x = input('Digite alguma coisa: ')
print(type(x))
print('É numerico, digito ou decimal? ', x.isnumeric())
print('É letra? ', x.isalpha())
print('Está em minusculo? ', x.islower())
print('Está em maiusculo? ', x.isupper())
print('É alfanumerico? ', x.isalnum())
print('É um numero?', x.isdigit())
print('É decimal?', x.isdecimal())

print('Mostra alguma coisa na tela? ',x.isprintable())
"""
s = 'Space is a printable'
print(s)
print(s.isprintable())

s = '\nNew Line is printable'
print(s)
print(s.isprintable())

s = ''
print('\nEmpty string printable?', s.isprintable())

saida 

Space is a printable
True

New Line is printable
False

Empty string printable? True
"""
