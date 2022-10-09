#Criar uma lista que leia 7 números e separar em duas listas com números impares e outra somente com os pares

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

#Guanabara fez
