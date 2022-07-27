# Existem tuplas, listas e dicionarios em python, nessa aula vamos estudar tuplas
# Tuplas são uma lista fixa de coisas e as TUPLAS SÃO IMUTÁVEIS ou seja, durante a
# execução da tuplas não dá para mudar o valor dos itens da lista

# Exemplo dos lanches

# Tuplas ficam entre () parenteses, listas entre [] colchetes e dicionario entre {} chaves

# Mostra todos os itens da tupla lanche
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim') # os parenteses são opcionais na nova versão do python
print(lanche)

# Mostra o primeiro item da tupla o hambúrguer
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[0]) # 0 Hambúrguer, 1 suco, 2 Pizza e 3 Pudim

# Para mostrar o hambúrguer posso colocar tanto 0 quanto -4
# 0 normal e -4 da frente para trás
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[-4]) # -4 Hambúrguer, -3 suco, -2 Pizza e -1 Pudim

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[0:2]) # Mostra sempre no final 1 a menos, ou seja, mostra o primeiro e o segundo

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1:3]) # Mostra suco e pizza

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[2:]) # Mostra do segundo até o final

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[:2]) # Mostra o elemento 0 e o 1, hambúrguer e suco

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[-3:]) # mostra do suco até o final, suco, pizza e pudim

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[:-1]) # Mostra até o penúltimo da tupla, hambúrguer, suco e pizza

# TUPLAS SÃO IMUTÁVEIS, ou seja, não da para atribuir valor
'''
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
lanche[1] = 'Refrigerante' # Essa linha causa um erro no programa
print(lanche[1])
'''


