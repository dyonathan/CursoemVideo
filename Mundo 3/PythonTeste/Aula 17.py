# na tupla () da erro porque a tupla é imutavel
'''
num = (2, 5, 9, 1)
num[2] = 3
print(num)

# Na lista [] já é mutável
num = [2, 5, 9, 1]
num[2] = 3 # troca o 9 na posição 2 pelo 3
print(num)
#num[4] = 7 # A lista só vai até à casa 3, no caso queria colocar um novo valor, más não é assim que funciona
num.append(7) # agora sim, adiciona um novo valor
print(num)

num.sort() # Coloca os valores em ordem crescente
print(num)

num.sort(reverse=True) # Coloca os valores em ordem decrescente
print(num)

print(len(num)) # Mostra quantos elementos tem na lista

num.insert(2, 2) # coloca o número 2 na posição 2 da lista
print(num)

#num.pop() # remove o ultimo valor da lista, no caso o 1

num.remove(2) # remove o primeiro número 2 da lista

# Na lista não tem o valor 4, se colocar num.remove(4) vai dar erro, por isso tem que verificar na lista antes de remover
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
'''


'''
valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

#print(valores) # dessa for mostra os valores [5, 9, 4], mas não quero mostrar entre colchetes
#Para resolver esse problema fazemos assim
#for v in valores:
#    print(f'{v}...', end='')

# Para mostrar o valor juntamente, com o índice(chave)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
'''

# Como falar os valores a serem colocados na lista
'''
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
'''

# mostra as duas listas
'''
a = [2, 3, 4, 7]
b = a

print(f'Lista A: {a}')
print(f'Lista B: {b}')
'''

'''
a = [2, 3, 4, 7]
b = a
b[2] = 8 # Adiciona o número 8 na posição 2 da lista b, mas...
print(f'Lista A: {a}')
print(f'Lista B: {b}')
# Quando imprimi às duas listas o valor da segunda posição mudou nas duas listas,
# isso porque quando coloca b = a ele não faz uma cópia da lista e sim uma ligação entre às duas
'''
'''
a = [2, 3, 4, 7]
b = a[:] # Fazendo esse fatiamento de string, ele não cria um link e sim uma cópia da string a para b
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
'''
# Enumerate

vendedores = ['Marcis', 'Amanda', 'Ale', 'Carol']
vendas = [15, 20, 10, 30]
