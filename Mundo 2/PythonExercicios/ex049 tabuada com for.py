# Fazer uma tabuada usando for

n = int(input('Qual a tabuada você deseja? '))
print('Tabuada'.center(10, ' '))
print('=-' * 6)
for c in range(0, 11):
    print('{} x {:2} = {}'.format(n, c, n * c))
print('=-' * 6)

# Guanabara fez igual, mas sem a tabulação antes e após a tabuada


