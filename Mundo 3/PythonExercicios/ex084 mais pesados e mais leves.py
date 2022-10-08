#Ler o nome e peso de n pessaos e motrar
#Quantas pessoas foram cadastradas
#O nome das pessoas com maior peso
#O nome das pessoas com menor peso

dados = []
pessoa = []
qtd = maispesado = 0
menospesado = 900

while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    op = str(input('Quer continuar? '))
    pessoa.append(dados[:])
    dados.clear()
    qtd += 1
    if op in 'Nn':
        break

for c in pessoa:
    if c[1] > maispesado:
        maispesado = c[1]

for c in pessoa:
    if c[1] < menospesado:
        menospesado = c[1]

print(f'Foram cadastradas {qtd} pessoas!')

for c in pessoa:
    if c[1] >= maispesado:
        print(f'{c[0]} é o mais pesado com {c[1]}!')

for c in pessoa:
    if c[1] <= menospesado:
        print(f'{c[0]} é o menos pesado com {c[1]}!')
