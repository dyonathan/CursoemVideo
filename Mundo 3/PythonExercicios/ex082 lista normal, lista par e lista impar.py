# Ler vários números em uma lista, criar mais duas uma com os números impares outro com os números pares

valores = list()
impar = list()
par = list()

while True:
    valores.append(int(input('Digite um valor: ')))

    op = ''

    op = str(input('Quer falar outro valor? [S/N] ')).strip().lower()
    if op == 'n':
        break


for c in range(0, len(valores)):
    if valores[c] % 2 != 0:
        impar.append(valores[c])
    else:
        par.append(valores[c])

print('-=' * 26)
print(f'A lista completa é {valores}')
print(f'Os valores pares foram {par}')
print(f'Os valores impares foram {impar}')
