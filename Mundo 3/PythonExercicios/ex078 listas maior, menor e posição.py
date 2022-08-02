# Guardar 5 valores uma lista e mostrar maior, menor e posição deles

maxi = 0
mini = 0

valores = list()
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    maxi = valores.count(max(valores))
    mini = valores.count(min(valores))

print(maxi)
print(mini)

print('=-' * 21)
print(f'Os valores digitados foram:{valores}')

print(f'O menor valor é {min(valores)} na posição: ', end=' ')
for c in range(0, mini):
    print(f'{valores.index(min(valores))}...')

print(f'\nO menor valor é {max(valores)} na posição: ', end=' ')
for c in range(0, maxi):
     print(f'{valores.index(max(valores))}...')


'''
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
'''