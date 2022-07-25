# while true executa para sempre e para, parar usa-se a flag break

# sem usar a while true
'''
n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
s -= 999
print('A soma vale {}'.format(s))
'''

# Usando o while true
'''
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}') # Usando f string
'''

#
nome = 'José'
idade = 33
salario = 987.35
print(f'O {nome:-^20} tem {idade} anos e ganha R${salario:.2f}.') # versão 3.6+
print('O {:-^20} tem {} anos e ganha R${}.'.format(nome, idade, salario)) # ANTIGO

