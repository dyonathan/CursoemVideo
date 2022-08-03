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
            break
        elif num > valores[0] < valores[1]:
            valores.insert(1, num)
            break
        elif num > valores[1] < valores[2]:
            valores.insert(2, num)
            break
        else:
            valores.insert(3, num)
            break
# 10 2 15 6 4
    print(c)
    print(valores[c])
    print(valores)



