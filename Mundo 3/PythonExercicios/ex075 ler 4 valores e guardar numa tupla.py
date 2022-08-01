# Ler 4 valores guardar numa tupla, mostrar quantos 9, posição do 3 e quais os pares

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))
n4 = int(input('Informe o quarto número: '))

numeros = (n1, n2, n3, n4)

print(f'Voce digitou os valores {numeros}')

print(f'O número 9 apareceu {numeros.count(9)} vezes!')
if 3 in (numeros):
    print(f'O número 3 aparece na {numeros.index(3) + 1}ª posição!')
else:
    print(f'O número 3 não foi digitado nenhuma vez!')

print(f'Os números pares foram ', end='')
for c in numeros:
    if c % 2 == 0:
        print(c, end=' ')

# Guanabara fez quase igual só mudou a tupla, ele colocou
'''
num = (int(input('Informe o primeiro número: ')),
       int(input('Informe o segundo número: ')),
       int(input('Informe o terceiro número: ')), 
       int(input('Informe o quarto número: ')))
'''