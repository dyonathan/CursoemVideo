#Criar uma lista que leia 7 números e separar em duas listas com números impares e outra somente com os pares
'''
temp = []
impar = []
par = []

for c in range(1, 8):
    temp.append(int(input(f'Digite o {c}º valor: ')))
    if temp[0] % 2 == 0:
        par.append(temp[0])
    else:
        impar.append(temp[0])
    temp.clear()

par.sort()
impar.sort()

print(f'Os valores pares digitados foram: {par}')
print(f'Os valores impares digitados foram: {impar}')
'''
#Guanabara fez

num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}o. valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valroes impares digitados foram: {num[1]}')
