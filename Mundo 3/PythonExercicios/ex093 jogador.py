#Pegar o nome do jogador, quantas partidas jogou e quantos gols marcou por partida e guardar os gols em uma lista

jogador = dict()
gols = list()


jogador['nome'] = str(input('Nome do jogador: '))
jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(1, jogos + 1):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)

print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {jogos} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')

#Fez igual