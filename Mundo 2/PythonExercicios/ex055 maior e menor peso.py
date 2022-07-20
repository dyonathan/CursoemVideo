# Ler o peso de 5 pessoas e mostrar o maior e o menor peso

maior = 0
menor = 999

print('Maior e menor peso!')
for c in range(0, 5):
    peso = float(input('Qual o peso da {}ª pessoa: '.format(c+1)))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior peso foi {}kg e o menor peso foi {}kg'.format(maior, menor))

# Guanabara fez igual, más ele fez um se para maior e menor receber o peso da primeira pessoa
'''
if c == 1:
    menor = peso
    maior = peso
'''