# Ler nome e preço em uma tupla, mostrar tabela de produtos

listagem = ('Pão', 3.00,
            'Leite', 5.00,
            'Frango', 40.00,
            'Arroz', 15.00,
            'Feijão', 8.00,
            'Mochila', 120.32)

print('-' * 30)
print('LISTAGEM DE PREÇOS'.center(30, ' '))
print('-' * 30)


for c in range(0, len(listagem), 2):
    print(f'{listagem[c]}'.ljust(20, '.'), f'R$ {listagem[c + 1]:>6.2f}')

print('-' * 30)


# Guanabara fez
'''
for pos in range(0 , len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)
'''