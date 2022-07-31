# Ler nome e preço em uma tupla, mostrar tabela de produtos

listagem = ('Pão', 3.00, 'Leite', 5.00, 'Frango', 40.00, 'Arroz', 15.00, 'Feijão', 8.00, 'Mochila', 120.32)

print('-' * 30)
print('LISTAGEM DE PREÇOS'.center(30, ' '))
print('-' * 30)

for c in range(0, len(listagem), 2):
    print(f'{listagem[c]}'.ljust(20, '.'), 'R$',  f'{listagem[c + 1]:.2f}'.rjust(6))

print('-' * 30)
