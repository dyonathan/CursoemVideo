#Para tuplas usa-se () para Listas usa-se [] e parra dicionarios usa-se {}
'''
dados = list()#Cria uma lista com o nome dados
dados.append('Pedro')#Adiciona o nome pedro na posição 0
dados.append(25)#Adiciona o numero 25 na posição 1
print(dados[0])#Mostra a posição 0 'Pedro'
print(dados[1])#Mostra a posição 1 25

#pode declarar dicionários ou dados=dict() ou dados={  }

#Fazendo a mesma declaração de cima mas com dicionário

dados = {'nome': 'Pedro', 'idade': 25}#Adiciona o nome e a idade no dicionário dados
print(dados['nome'])#Mostra o campo nome do dicionário
print(dados['idade'])#Mostra o campo idade

#Para adicionar um novo elemento não precisa usar o append é sou usar o
dados['sexo'] = 'M'
print(dados)

#Para remover um campo é só usar o
del dados['idade']
print(dados)


#Cadastra star wars no campo titulo, 1977 no campo ano e george lucas no campo diretor
filme = {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}

print(filme.values())#Retorna o valor do dicionário, 1º star wars, 2º 1977 e 3º George Lucas
print(filme.keys())#Retorna as chaves ou seja 1º titulo, 2º ano e 3º diretor
print(filme.items())#Retorna os 2 tanto os valores quanto as chaves

for k, v in filme.items():
    print(f'O {k} é {v}')
#1º mostra: O titulo é Star Wars
#2º mostra: O ano é 1977
#3º mostra: O diretor é George Lucas
'''

locadora = list()
filme1 = {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}
filme2 = {'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedon'}
filme3 = {'titulo': 'Matrix', 'ano': 1999, 'diretor': 'Wachowski'}

locadora.append(filme1)
locadora.append(filme2)
locadora.append(filme3)

print(locadora[0]['ano'])#Mostra ano do campo 0 da locadora 1977
print(locadora[2]['titulo'])#Mostra titulo do campo 2 da locadora Matrix


