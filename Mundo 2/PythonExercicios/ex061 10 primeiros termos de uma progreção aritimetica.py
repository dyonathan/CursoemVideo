# Progressão aritmética

primeiro = int(input('Qual o primeiro termo? '))
razao = int(input('Qual a razão da PA? '))

decimo = primeiro + (10 - 1) * razao

while primeiro < decimo + razao:
    print(primeiro, end=' -> ')
    primeiro += razao

print('Fim')
