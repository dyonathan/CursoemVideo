#Criar uma matriz 3x3 e mostrar
#Soma dos pares
#Soma da terceira coluna
#e o maior valor da segunda linha
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = ter = seg = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[c][l] = int(input(f'Digite um valor para [{l}, {c}]: '))

for l in range(0, 3):
    for c in range(0, 3):
        if matriz[c][l] % 2 == 0:
            par += matriz[c][l]
        if c == 2:
            ter += matriz[c][l]
        if l == 1:
            if matriz[c][l] > seg:
                seg = matriz[c][l]

print('-=' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[c][l]:^5}]', end='')
    print()
print('-=' * 20)
print(f'A soma dos valores pares é {par}.')
print(f'A soma dos valores da terceira coluna é {ter}.')
print(f'O maior valor da segunda linha é {seg}.')
'''

#Guanabara fez

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = scol = mai = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira colune é {scol}.')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')
