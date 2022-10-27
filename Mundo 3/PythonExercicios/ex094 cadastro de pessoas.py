#Ler nome, sexo e idade de n pessoas
#Guardar cada pessoa em um dicionario e todos os dicionarios em uma lista
#mostrar, qtd de cadastros, média de idade do grupo, lista com todas as mulheres e uma lista com todas as pessoas com idade acima da média
'''
import copy

cadastro = []
pessoa = {}
sidade = media = teste = 0

while True:
    pessoa['nome'] = str(input('nome: '))
    while True:
        pessoa['sexo'] = str(input('sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] not in 'MmfF':
            print('Sexo invalido, tente novamente!')
        else:
            break
    pessoa['idade'] = int(input('Idade: '))
    cadastro.append(pessoa.copy())
    sidade += pessoa['idade']
    while True:
        op = str(input('Quer Continuar? [S/N] ')).upper()[0]
        if op not in 'SsNn':
            print('Opção invalida, tente novamente!')
        else:
            break
    if op in 'Nn':
        break

media = sidade / len(cadastro)

print('-=' * 30)
print(cadastro)
print(f'- O grupo tem {len(cadastro)} pessoas.')
print(f'- A média de idade é de {media:5.2f} anos.')
print('- As mulheres cadastradas foram:', end=' ')

for p in cadastro:
    if p['sexo'] in 'Ff':
        print(p['nome'], end=' ')
print()

print(f'- Lista das pessoas que estão acima da média: ')

for p in cadastro:
    if p['idade'] > media:
        print(f'    nome = {p["nome"]}; sexo = {p["sexo"]}; idade = {p["idade"]};')

print('<< ENCERRADO >>')
'''

#Guanabara fez

galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
