# Ler idade e sexo de várias pessoas. Perguntar se quer parar, quando parar
# mostrar quantos com menos de 18, quantos homens cadastrados e quantas mulheres com menos de 20 anos

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

