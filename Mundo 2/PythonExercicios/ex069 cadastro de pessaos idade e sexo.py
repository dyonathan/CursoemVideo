# Ler idade e sexo de várias pessoas. Perguntar se quer parar, quando parar
# mostrar quantos com menos de 18, quantos homens cadastrados e quantas mulheres com menos de 20 anos
'''
continuar = 'J'
mais18 = 0
tothomens = 0
mulheres20 = 0

while True:
    if continuar[0] == 'N':
        break
    else:
        idade = int(input('Qual a sua idade: '))
        sexo = 'J'

        while True:
            if sexo[0] == 'M' or sexo[0] == 'F':
                break
            else:
                sexo = str(input('Qual seu sexo[M/F]: ')).strip().upper()

        if idade > 18:
            mais18 += 1

        if sexo[0] == 'M':
            tothomens += 1

        if sexo[0] == 'F' and idade < 20:
            mulheres20 += 1

        continuar = 'J'

        while True:
            if continuar[0] == 'N' or continuar[0] == 'S':
                break
            else:
                continuar = str(input('Quer cadastrar mais pessoas[S/N]: ')).strip().upper()

print(f'{mais18} Pessoas tem mais de 18 anos!')
print(f'{tothomens} homens foram cadastrados!')
print(f'{mulheres20} mulheres com menos de 20 anos foram cadastradas!')
'''

# Guanabara fez

tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados.')
print(f'E temos {totM20} mulheres com menos de 20 anos.')
