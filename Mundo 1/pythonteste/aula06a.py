# soma de dois numeros
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
s = n1 + n2

# print('A soma entre ', n1, ' e ', n2, ' vale: ', s) esse é o formato antigo do python 2

print('A soma entre {} e {} vale {}'.format(n1, n2, s)) # novo formato python 3

