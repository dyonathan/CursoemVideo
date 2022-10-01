# Ler vários números em uma lista, criar mais duas uma com os números impares outro com os números pares
'''
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
'''
#Guanabara fez

num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
