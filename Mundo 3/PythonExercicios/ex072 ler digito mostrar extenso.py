# Tupla que lê digito de 0 a 20 e mostrar por extenso

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

numero = int(input('Digite um número entre 0 e 20: '))

while True:
    if numero >= 0 and numero <= 20:
        print(f'Você digitou o número {extenso[numero]}')
        break
    else:
        numero = int(input('Tente novamente. Digite um número entre 0 e 20: '))

# Guanabara fez
'''
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
            break
        print('Tente novamente. ', end='')
print(f'Você digitou o número {extenso[num]}')
'''