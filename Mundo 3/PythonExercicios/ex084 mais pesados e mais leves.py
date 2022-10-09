#Ler o nome e peso de n pessaos e motrar
#Quantas pessoas foram cadastradas
#O nome das pessoas com maior peso
#O nome das pessoas com menor peso
'''
dados = []
pessoa = []
qtd = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    op = str(input('Quer continuar? '))
    pessoa.append(dados[:])
    dados.clear()
    if len(pessoa) == 1:
        maispesado = menospesado = pessoa[0][1]
    if op in 'Nn':
        break

for c in pessoa:
    if c[1] > maispesado:
        maispesado = c[1]
    if c[1] < menospesado:
        menospesado = c[1]


print(f'Foram cadastradas {len(pessoa)} pessoas!')

for c in pessoa:
    if c[1] >= maispesado:
        print(f'{c[0]} é o mais pesado com {c[1]}!')

for c in pessoa:
    if c[1] <= menospesado:
        print(f'{c[0]} é o mais leve com {c[1]}!')
'''
#Guanabara fez

temp = []
princ = []
ami = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas!')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()

