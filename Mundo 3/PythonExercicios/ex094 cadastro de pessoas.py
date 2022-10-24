#Ler nome, sexo e idade de n pessoas
#Guardar cada pessoa em um dicionario e todos os dicionarios em uma lista
#mostrar, qtd de cadastros, média de idade do grupo, lista com todas as mulheres e uma lista com todas as pessoas com idade acima da média
import copy

cadastro = []
pessoa = {}
media = 0
sidade = 0
teste = 0

while True:
    pessoa['nome'] = str(input('nome: '))
    pessoa['sexo'] = str(input('sexo: [M/F] '))
    pessoa['idade'] = int(input('Idade: '))
    op = str(input('Quer Continuar? [S/N] '))
    cadastro.append(pessoa.copy())
    sidade += pessoa['idade']
    if op in 'Nn':
        break

media = sidade / len(cadastro)

print('-=' * 30)
print(pessoa)
print(cadastro)
print(f'- O grupo tem {len(cadastro)} pessoas.')
print(f'- A média de idade é de {media} anos.')
print('- As mulheres cadastradas foram:', end=' ')

for p in cadastro:
    if p['sexo'] in 'Ff':
        print(p['nome'], end=' ')
print()

print(f'- Lista das pessoas que estão acima da média: ')

for p in cadastro:
    if p['idade'] > media:
        print()
        print(f'nome = {p["nome"]}; sexo = {p["sexo"]}; idade = {p["idade"]};')

print('<< ENCERRADO >>')
