# Ler o ano de nascimento de 7 pessoas e mostrar quantos maior e quantos menores de 21

from datetime import date

maior = 0
menor = 0

print('Maiores e menores de 21 anos!')
for c in range(0, 7):
    nasc = int(input('Qual o ano de nascimento? '))
    idade = date.today().year - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1

print('São {} pessoas maiores de 21 anos e {} pessoas menores!'.format(maior, menor))
