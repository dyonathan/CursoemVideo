'''
dados = list()# ou dados = [] cria uma lista chamada dados
dados.append('Pedro')# Adiciona Pedro naposição 0
dados.append(25)# Adiciona 25 na posição 1
print(dados[0])# Mostra Pedro
print(dados[1])# Mostra 25
'''

dados = list()
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]# Cria 3 listas com 2 indicis cada
'''
dados.append('Pedro')# Adiciona Pedro naposição 0
dados.append(25)# Adiciona 25 na posição 1
'''

pessoas.append(dados[:])# faz um fatiamento(uma cópia) da lista dados
print(pessoas[0][0])# Mosta a pessa 0 no item 0 ou seja Pedro
print(pessoas[1][1])# Mosta a pesso 1 no item 1 ou seja 19
print(pessoas[2][0])# Mostra a pessoa 2 no item 0 ou seja João
print(pessoas[1])# Mostra o item 1 ou seja ['Maria', 19]

