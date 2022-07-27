# Ler o nome e o preço de vários produtos e perguntar se quer continuar, no final
# mostrar total gasto, quantos custam mais de 1000 e nome do mais barato
'''
nomebarato = 'J'
continuar = 'J'
totalgasto = 0
maisdemil = 0
precobarato = 0

print('-' * 30)
print('{:-^30}'.format('LOJA SUPER BARATÃO'))
print('-' * 30)

while True:
    if continuar[0] == 'N':
        break
    else:
        nome = str(input('Nome do produto: '))
        preco = float(input('Qual o preço: R$'))

        totalgasto += preco

        if preco > 1000:
            maisdemil += 1

        if precobarato == 0 and nomebarato == 'J':
            precobarato = preco
            nomebarato = nome
        elif preco < precobarato:
            precobarato = preco
            nomebarato = nome

        continuar = 'J'
    while True:
        if continuar[0] == 'N' or continuar[0] == 'S':
            break
        else:
            continuar = str(input('Quer continuar? [S/N] ')).strip().upper()

print('----------- FIM DO PROGRAMA -------------')
print(f'O total gasto nas compras foi R${totalgasto:.2f}!')
print(f'{maisdemil} Produtos custaram mais de R$1000!')
print(f'{nomebarato} e ele custou R${precobarato:.2f}!')
'''

# Guanabara fez

total = totmil = menor = cont = 0
batato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
