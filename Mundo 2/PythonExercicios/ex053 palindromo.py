# Ler uma frase e ver se ela é um palíndromo
'''
frase = str(input('Qual a frase? ')).strip().upper().split()
junto = ''.join(frase)
contra = ''

for c in range(len(junto)-1, -1, -1):
    contra += junto[c]

print('Normal é {} ao contrario é {}!'.format(junto, contra))

if contra == junto:
    print('Essa palavra é um palindromo!')
else:
    print('Essa palavra não é um palindromo!')
'''

# Guanabara fez

frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
