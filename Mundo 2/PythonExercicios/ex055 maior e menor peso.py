# Ler o peso de 5 pessoas e mostrar o maior e o menor peso

maior = 0
menor = 999

print('Maior e menor peso!')
for c in range(0, 5):
    peso = float(input('Qual o peso? '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior peso foi {}kg e o menor peso foi {}kg'.format(maior, menor))
