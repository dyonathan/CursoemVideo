# Progressão aritmética
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
