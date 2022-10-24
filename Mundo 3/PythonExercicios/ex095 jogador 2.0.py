#Melhorar o ex93 e fazer o cadastro de varios jogadores e mostrar detalhado cada jogador

jogador = dict()
gols = list()
jogadores = list()
golsp = list()
temp = list()
totgol = 0


while True:
    print('-' * 30)
    nome = str(input('Nome do jogador: '))
    jogos = int(input(f'Quantas partidas {nome} jogou? '))
    for c in range(1, jogos + 1):
        gol = int(input(f'Quantos gols na partida {c}? '))
        golsp.append(golsp.copy(gol))
        totgol += gol
    print(golsp)
    jogadores.append([nome, golsp, totgol])
    totgol = 0
    temp.clear()
    print(jogadores)
    op = str(input('Quer continuar? [S/N] '))
    if op in 'Nn':
        break

jogador['gols'] = golsp
jogador['total'] = totgol

print('-=' * 30)
print(jogador)
print(jogadores)
print('-=' * 30)
print(f'{"cod":<4}{"nome":<15}{"gols":<15}{"total":>10}')
print('-' * 45)
#for c, v in enumerate(jogadores):
 #   print(c)

'''
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {jogos} partidas.')
for c in range(1, jogos + 1):
    print(f'   => Na partida {c}, fez {golsp[c-1]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
'''
