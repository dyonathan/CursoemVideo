# Perguntar o valor a sacar e mostrar
# Quantas notas de 50, 20, 10 e 1 vao sair

from math import floor

n50 = 0
n20 = 0
n10 = 0
n1 = 0
resto = 0

print('=' * 30)
print('          BANCO CEV')
print('=' * 30)

valor = float(input('Quanto você quer sacar? R$'))

if valor != 0:
    n50 = (valor / 50)
    resto = valor % 50
    print(f'{floor(n50)} notas de R$50,00')

if resto != 0:
    n20 = (resto / 20)
    resto = resto % 20
    print(f'{floor(n20)} notas de R$20,00')

if resto != 0:
    n10 = (resto / 10)
    resto = resto % 10
    print(f'{floor(n10)} notas de R$10,00')

if resto != 0:
    n1 = (resto / 1)
    resto = resto % 1
    print(f'{floor(n1)} notas de R$1,00')

print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')



