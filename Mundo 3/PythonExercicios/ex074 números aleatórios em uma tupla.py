# Gerar cinco números aleatórios e colocar em uma tupla
# mostrar a listagem de números, o menor e o maior

from random import randint

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(f'Os valores sorteados foram:', end=' ')
for c in range(0, 5):
    if c == 0:
        maior = numeros[0]
        menor = numeros[0]

    if numeros[c] > maior:
        maior = numeros[c]
    if numeros[c] < menor:
        menor = numeros[c]

    print(numeros[c], end=' ')

print('')
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
