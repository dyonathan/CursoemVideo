'''
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])# Esse [:] cria uma copia da lista sem ele esse codigo gera uma ligação entre os 2 e tudo que mudar em um muda no outro
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(teste)
print(galera)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)# Mostra toda a lista
print(galera[0])# Mostra joão 19
print(galera[0][0])#Mosta so joao

for pessoa in galera:# Mostra todos os nomes da lista galera
    print(pessoa[0])

for pessoa in galera:# Mostra todas as idades da lista galera
    print(pessoa[1])

for pessoa in galera:# Mostra a mensagem com o nome e a idade de todos
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')
'''

galera = []# Cria a lista galera
dado = []
totmai = totmen = 0
for contador in range(0, 3):# Repete 3 vezes
    dado.append(str(input('Nome: ')))# Pega o nome
    dado.append(int(input('Idade: ')))# Pega a idade
    galera.append(dado[:])# Passa os dados para a lista galera
    dado.clear()# Limpa a lista dado

print(galera)# Mostra os dados da galera
# [['Pedro', 22], ['Maria', 33], ['Claudia', 55]]

for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')

