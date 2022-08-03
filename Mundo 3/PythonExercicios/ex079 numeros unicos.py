# Ler n números, se for repetido pedir outro número, no final mostrar por ordem crescente

valores = list()
c = 0

while True:
    n = valores
    num = int(input('Digite um valor: '))

    if num in n:
        print('Valor duplicado! Não vou adicionar...')
    else:
        valores.append(int(num))
        print('Valor adicionado com sucesso...')

    c += 1
    op = str(input('Quer digitar outro valor? [S/N] ')).strip()
    if op[0] in 'Nn':
        break


valores.sort()
print('-=' * 20)
print(f'Você digitou os valores {valores}')
