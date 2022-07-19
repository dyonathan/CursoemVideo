# Ler seis números inteiros e mostrar a soma dos valores pares.

s = 0

print('Soma dos números pares')
print('-=' * 15)

for c in range(0, 6):
    n = int(input('Quais números: '))
    if n % 2 == 0:
        s += n

print('A soma dos números pares é {}'.format(s))

# Guanabara fez igual, mas ele contou a quantidade de números somados
