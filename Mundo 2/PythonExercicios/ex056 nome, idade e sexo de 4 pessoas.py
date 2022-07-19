# Ler o nome, idade e sexo de 4 pessoas e mostrar média de idade, o homem mais velho e quantas mulheres com menos de 20 anos

sidade = 0
velho = 0
menos = 0

print('Dados pessoais')
for c in range(0, 4):
    nome = str(input('Qual o nome? ').strip())
    idade = int(input('Qual a idade? '))
    sexo = str(input('''M para masculino
F para feminino
Qual: ''').strip().upper())

    sidade += idade

    if idade > velho:
        velho = idade
        mvelho = nome

    if sexo == 'F' and idade < 20:
        menos += 1

print('A média de idade foi {} anos!'.format(sidade/4))
print('O homem mais velho foi o {}!'.format(mvelho))
print('Foram {} mulheres com menos de 20 anos!'.format(menos))
