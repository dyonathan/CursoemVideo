# Guardar 5 valores uma lista e mostrar maior, menor e posição deles

valores = list()
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))

print('=-' * 21)
print(f'Os valores digitados foram:{valores}')

print(f'O menor valor é {max(valores)} nas posições: ', end='')
for c in range(0, len(valores)):
     if valores[c] == max(valores):
        print(f'{c}...', end=' ')

print(f'\nO menor valor é {min(valores)} nas posições: ', end='')
for c in range(0, len(valores)):
    if valores[c] == min(valores):
        print(f'{c}...', end=' ')


