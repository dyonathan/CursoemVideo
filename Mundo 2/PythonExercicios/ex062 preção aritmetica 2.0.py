# Progressão aritmética
'''
op = 1
primeiro = int(input('Qual o primeiro termo? '))
razao = int(input('Qual a razão da PA? '))
qtd = int(input('Quantos termos? '))

decimo = primeiro + (10 - 1) * razao

while qtd != 0:
    for c in range(primeiro, primeiro + qtd):
        print(primeiro)
        primeiro += razao
    qtd = int(input('Ver mais quantas progressões?  (0 para sair)? '))

print('Fim')
'''

# Guanabara fez


print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))

