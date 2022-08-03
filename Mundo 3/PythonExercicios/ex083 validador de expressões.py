# ler expressão que use parenteses, olhar se os parenteses estão corretos

expressao = list()

asd = str(input('Fale uma expressão aritmetica: ')).strip().lower()
sequencia = asd.split()

for c in range(0, len(sequencia)):
    print('(' in sequencia)
    print(')' in sequencia)
    print(sequencia)

print(sequencia)
print(sequencia[1])
print(sequencia[1])
print(len(sequencia))
