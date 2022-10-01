# Ler vários números mostrar, qtd, ordem decrescente e se tem o 5 na lista
'''
valores = list()

while True:
    valores.append(int(input('Digite um valor: ')))
    op = str(input('Quer Continuar? [S/N] ')).strip().lower()
    if op in 'Nn':
        break

valores.sort(reverse=True)

print('-=' * 26)
print(f'Foram lidos {len(valores)} números!')
print(f'A ordem decrescente foi {valores}')
if 5 in valores:
    print(f'Avia o número 5 na lista!')
else:
    print('Não avia o número 5 na lista!')
'''
#Guanabara fez

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('=-' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
