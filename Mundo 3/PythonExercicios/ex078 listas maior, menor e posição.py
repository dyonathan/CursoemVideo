# Guardar 5 valores uma lista e mostrar maior, menor e posição deles

'''
valores = list()

for c in range(5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))

print('=-' * 21)
print(f'Os valores digitados foram:{valores}')

print(f'O maior valor é {max(valores)} nas posições: ', end='')
for c in range(len(valores)):
     if valores[c] == max(valores):
        print(f'{c}...', end=' ')

print(f'\nO menor valor é {min(valores)} nas posições: ', end='')
for c in range(len(valores)):
    if valores[c] == min(valores):
        print(f'{c}...', end=' ')

print()
'''

# Guanabara fez

listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()

