# Ler n números, se for repetido pedir outro número, no final mostrar por ordem crescente

valores = list()

while True:

    num = int(input('Digite um valor: '))

    if num in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        valores.append(int(num))
        print('Valor adicionado com sucesso...')

    op = str(input('Quer digitar outro valor? [S/N] ')).strip()
    if op[0] in 'Nn':
        break

valores.sort()
print('-=' * 20)
print(f'Você digitou os valores {valores}')
'''
# Guanabara fez

numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor Adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-' * 30)
numeros.sort()
print(f'Você digitou os valores {numeros}')
'''