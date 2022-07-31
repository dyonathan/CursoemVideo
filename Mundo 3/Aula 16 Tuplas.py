# Existem tuplas, listas e dicionarios em python, nessa aula vamos estudar tuplas
# Tuplas são uma lista fixa de coisas e as TUPLAS SÃO IMUTÁVEIS ou seja, durante a
# execução da tuplas não dá para mudar o valor dos itens da lista

# Exemplo dos lanches

# Tuplas ficam entre () parenteses, listas entre [] colchetes e dicionario entre {} chaves
'''
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

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
lanche[1] = 'Refrigerante' # Essa linha causa um erro no programa
print(lanche[1])

# "Mostra eu vou comer" e o nome da comida na frente, primeiro hambúrguer, depois suco e assim por diante
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

# essa é a forma básica de se fazer
for comida in lanche:
    print(f'Eu vou comer {comida}')

# Forma avançada
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')

# Com contador de posição
# Usando len(contador)
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

# Usando enumerate de lanche
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!')

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

# Coloca em ordem alfabética os itens da tupla
print(sorted(lanche))

# soma de tuplas
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b # Mostra tuplas A depois a B junta
# 2, 5, 4, 5, 8, 1, 2
print(c)

print(c.count(5))# Conta quantos 5 tem na tupla c
print(c.index(8))# Mostra em qual posição está número 8 aqui no 4 porque começa no 0
print(c.index(2))# Mostra a posição do primeiro número 2 ou sejá 0
print(c.index(2, 1))# Mostra a posição do primeiro número 2 começando a procurar na posição 1 ou seja 6 porque o primeiro está no 0 e o segundo no 6

# O python permite tuplas com mais de um tipo de dado, int, floor, str, etc.
pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)
'''

pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa) # deleta momentaneamente a tupla pessoa
del(pessoa[0])# Teoricamente iria excluir somente a posição 0 da tupla, más as tuplas são imutaveis, ou exclui tudo ou nada
print(pessoa)
