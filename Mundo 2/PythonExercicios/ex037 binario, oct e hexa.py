# Converter para binário, Octal ou hexadecimal
'''
print('Converter para binário, octal ou hexadecimal...')
n = int(input('Qual valor deseja converter? '))
op = int(input(''''''1 - Binário
2 - Octal
3 - Hexadecimal
Qual a escolha? ''''''))

if op == 1:
    print('{} em binário fica {}'.format(n, bin(n)))
elif op == 2:
    print('{} em Octodecimal fica {}'.format(n, oct(n)))
elif op == 3:
    print('{} em hexadecimal fica {}'.format(n, hex(n)))
else:
    print('Opção inválida')
'''

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))

# O [2:] no final é para começar no terceiro caractere, no bin tira o 0b
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida! Tente novamente.')
