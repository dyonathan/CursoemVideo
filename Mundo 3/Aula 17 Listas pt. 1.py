# As listas diferentes das tuplas podem ser mudadas

#lache = ('sanduíche', 'suco', 'pizza', 'pudim') # isso é uma tupla esta entre () parenteses

lanche = ['sanduíche', 'suco', 'pizza', 'pudim'] # Isso é uma lista está entre [] colchetes
lanche[3] = 'picolé' # Troco o pudim pelo picolé oque é impossível em uma tupla
lanche.append('cockie') # Adiciona cookie no final da lista de lanches
lanche.insert(0, 'cachorro-quente') # Adiciona cachorro-quente na posição 0 da lista e passa o restante para frente nas chaves ou seja o picolé que tava na posição 3 foi para a 4
#del lanche[3] # exclui o item da chave 3 da lista lanche a pizza
#lanche.pop(3) # Também exclui item da lista se deixa vazio o pop ele exclui o último item da lista
lanche.remove('pizza') # Exclui o item especifico indicado no remove

# se não existir o item na lista para excluir dá erro, por isso usa um if para verificar
if 'pizza' in lanche:
    lanche.remove('pizza')

print(lanche)

# Criando lista atravez de range

valores = list(range(4, 11)) # Cria uma lista com os números de 4 a 10
print(valores)

valores1 = [8, 2, 5, 4, 9, 3, 0] # Cria uma lista desordenada de valores
print(valores1)

valores1.sort() # Coloca os valores em ordem antes de mostrar
print(valores1)

valores1.sort(reverse=True) # Cria uma lista em ordem decrescente
print(valores1)

print(len(valores1)) # mostra o tamanho da lista
