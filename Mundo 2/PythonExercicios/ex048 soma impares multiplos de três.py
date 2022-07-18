# Somo todos os ímpares múltiplos de três de 1 até 500
s = 0
print('Soma os números ímpares que são multiplos ')
for c in range(0, 500, 3):
    if c % 3 == 0:
        s += c
print('A soma deu: {}'.format(s))
