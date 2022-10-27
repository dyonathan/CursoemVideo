#Melhorar o ex93 e fazer o cadastro de varios jogadores e mostrar detalhado cada jogador
'''
jogador = dict()
gols = list()
selecao = list()
golsp = list()
temp = list()
totgol = 0


while True:
    gols.clear()
    print('-' * 30)
    jogador['nome'] = str(input('Nome do jogador: '))
    jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(1, jogos + 1):
        gols.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    selecao.append(jogador.copy())
    op = str(input('Quer continuar? [S/N] ')).upper()[0]
    if op in 'Nn':
        break

print('-=' * 30)
print(f'{"cod":<4}{"nome":<15}{"gols":<15}{"total":>10}')
print('-' * 45)
print(jogador)
print(selecao)
'''
'''
for i, v in enumerate(selecao):
    print(f'{i} = {v[selecao]}', end='')
'''

#Guanabara fez

time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'Nn':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
