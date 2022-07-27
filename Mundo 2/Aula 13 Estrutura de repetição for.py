# Fazer 10 passos no for

'''
for c in range(1, 10):
    passo
pega
'''

# Fazer passos com pulos
'''
for c in range(0, 3):
    passo
    pula
passo
pega
'''

# Pegar moedas no meio do pulo
'''
for c in range(0, 3):
    if moeda:
        pega
    passo
    pula
passo
passo
'''

# Parte pratica

# Escrever oi 6 vezes
'''
for c in range(0, 6):
    print('Oi')
print('Fim')
'''

# Faz uma contagem regressiva de 6 ate 0
'''
for c in range(6, 0, -1):
    print(c)
print('Fim')
'''

# Faz uma contagem de 0 a 6 pulando de 2 em 2
'''
for c in range(0, 7, 2):
    print(c)
print('FIM')
'''

# Conta de 0 até o número digitado
'''
n = int(input('Digite um número: '))
for c in range(0, n + 1):
    print(c)
print('FIM')
'''

# Conta do início, até o fim pulando os passos

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f + 1, p):
    print(c)
print('FIM')


# soma de 4 números

# inicializa a variável s
'''
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    # O mesmo que s = s + n
    s += n
print('O somatório de todos os valores foi {}'.format(s))
'''
