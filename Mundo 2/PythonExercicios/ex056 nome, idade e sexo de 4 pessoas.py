# Ler o nome, idade e sexo de 4 pessoas e mostrar média de idade, o homem mais velho e quantas mulheres com menos de 20 anos
'''
sidade = 0
velho = 0
menos = 0

print('Dados pessoais')
for c in range(0, 4):
    print('--- {}ª PESSOA ----'.format(c + 1))
    nome = str(input('Qual o nome? ').strip())
    idade = int(input('Qual a idade? '))
    sexo = str(input('Sexo [M/F]: ').strip().upper())

    if sexo == 'M' or sexo == 'F':
        sidade += idade

        if idade > velho:
            velho = idade
            mvelho = nome

        if sexo == 'F' and idade < 20:
            menos += 1
    else:
        print('Sexo Invalido!!!')

print('A média de idade foi {} anos!'.format(sidade/4))
print('O homem mais velho foi o {}!'.format(mvelho))
print('Foram {} mulheres com menos de 20 anos!'.format(menos))
'''

# Guanabara fez

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('---- {}ª PESSA ----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))
