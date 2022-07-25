# Progressão aritmética
'''
primeiro = int(input('Qual o primeiro termo? '))
razao = int(input('Qual a razão da PA? '))

decimo = primeiro + (10 - 1) * razao

while primeiro < decimo + razao:
    print(primeiro, end=' -> ')
    primeiro += razao

print('Fim')
'''

# Guanabara fez

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
