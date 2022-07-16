# Converter para binário, Octal ou hexadecimal

print('Converter para binário, octal ou hexadecimal...')
n = int(input('Qual valor deseja converter? '))
op = int(input('''1 - Binário
2 - Octal
3 - Hexadecimal
Qual a escolha? '''))

if op == 1:
    print('{} em binário fica {}'.format(n, bin(n)))
elif op == 2:
    print('{} em Octodecimal fica {}'.format(n, oct(n)))
elif op == 3:
    print('{} em hexadecimal fica {}'.format(n, hex(n)))
else:
    print('Opção inválida')
