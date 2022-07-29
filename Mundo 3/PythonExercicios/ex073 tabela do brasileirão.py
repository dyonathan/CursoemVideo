# colocar a ordem de colocação do brasileirão depois mostrar
# os 5 primeiros, os 4 últimos, ordem alfabética e posição da chapecoense.

brasileirao = ('Palmeiras', 'Corinthians', 'Fluminense', 'Atlético-MG', 'Atlético-PR', 'Flamengo', 'Internacional', 'Bragantino', 'Santos', 'São Paulo', 'Botafogo', 'Ceará SC', 'Coritiba', 'Goiás', 'América-MG', 'Avaí', 'Cuiabá', 'Atlético-GO', 'Juventude', 'Fortaleza')

print('Hoje é 29/07/2022')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {brasileirao}')

print('-=' * 15)
print(f'Os 5 primeiros são {brasileirao[:5]}')

print('-=' * 15)
print(f'Os 4 últimos são {brasileirao[-4:]}')


print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(brasileirao)}')


print('-=' * 15)
for pos, time in enumerate(brasileirao):
    if brasileirao[pos] == 'Bragantino':
        print(f'O Bragantino está na {pos + 1}ª posição!')
