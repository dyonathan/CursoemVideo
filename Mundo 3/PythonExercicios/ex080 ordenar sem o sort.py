# Digitar 5 valores colocar na lista já na ordem numérica sem usar o sort

valores = list()
reserva = list()

num = int(input(f'Digite o 1ª valor: '))
print('Adicionado ao final da lista...')

valores.append(num)

for c in range(0, 4):
    num = int(input(f'Digite o {c + 2}ª valor: '))
    for c1 in range(0, len(valores)):
        if num >= max(valores):
            valores.append(num)
            print('Adicionado ao final da lista...')
            break
        elif num <= min(valores):
            valores.insert(0, num)
            print('Adicionado na posição 0 da lista...')
            break
        elif num > valores[0] and num < valores[1]:
            valores.insert(1, num)
            print('Adicionado na posição 1 da lista...')
            break
        elif num > valores[1] and num < valores[2]:
            valores.insert(2, num)
            print('Adicionado na posição 2 da lista...')
            break
        else:
            valores.insert(3, num)
            print('Adicionado na posição 3 da lista...')
            break

print('-=' * 26)
print(f'Os valores digitados em ordem foram {valores}')



