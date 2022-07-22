# Ler n números até digitar 999, falar quantos números foram digitados e a soma deles

n = 0
cont = 0
soma = 0

while n != 999:
    n = int(input('Digite um número ou 999 para sair: '))
    if n != 999:
        cont += 1
        soma += n

print('Foram digitados {} número(s) e a soma dele(s) foi {}!!'.format(cont, soma))
