# Somo todos os ímpares múltiplos de três de 1 até 500
'''
s = 0
print('Soma os números ímpares que são múltiplos de 3')
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
print('A soma deu: {}'.format(s))
'''

# Guanabara fez, ele acrescentou o quantos números foram

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
