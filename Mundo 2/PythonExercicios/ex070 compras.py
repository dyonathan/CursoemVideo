# Ler o nome e o preço de vários produtos e perguntar se quer continuar, no final
# mostrar total gasto, quantos custam mais de 1000 e nome do mais barato

nomebarato = 'J'
continuar = 'J'
totalgasto = 0
maisdemil = 0
precobarato = 0

print('-' * 30)
print('     LOJA SUPER BARATÃO')
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
