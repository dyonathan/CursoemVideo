# Escreve olá, mundo! em negrito (codigo 1), com a cor vermelha (codigo 31) e o fundo amarelo (Codigo 43) e coloca o \033[m no final para o fundo amarelo não ir até o fim da linha.
print('\033[1;31;43mOlá, mundo!\033[m')

# Exemplo no programa

a = 3
b = 5
# primeiro numero vermelho e segundo verde usando ANSI no texto
print('Os valores são \033[31m{}\033[m e \033[32m{}\033[m!!!'.format(a, b))

# muda a cor usando o format do texto para não fica como no exemplo de cima, nesse coloquei letra em negrito
nome = 'Dyonathan'
print('Muito prazer em te conhecer, {}{}{}!!!'.format('\033[1;40m', nome, '\033[m'))

# Faz um dicionário de cores, o limpa finaliza para não seguir para o resto
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}

# No format coloca o nome da lista e o item da lista
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format(cores['amarelo'], nome, cores['limpa']))

s = 3*5+4**2
d = 19%2
print(s,d)