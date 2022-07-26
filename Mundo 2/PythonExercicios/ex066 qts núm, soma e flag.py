# ler n números fazer a soma, falar quantos foram e usar flag e break
n = 0
cont = 0
soma = 0

while True:
    n = int(input('Digite um número ou 999 para sair: '))
    if n == 999:
       break
    cont += 1
    soma += n

print('Foram digitados {} número(s) e a soma dele(s) foi {}!!'.format(cont, soma))

# Guanabara fez igual
