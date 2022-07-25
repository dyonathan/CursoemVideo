# Lêr vários números falar a média deles, qual foi o maior, o menor e só parar quando digitar para parar

continuar = ''
cont = 0
soma = 0

while continuar != 'n':
    n = int(input('Digite um número inteiro: '))

    cont += 1
    soma += n

    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    continuar = str(input('Continuar [S/N]? ')).lower().strip()

media = soma/cont
print('Você informou {} números, a média deles foi {:.2f}, o maior foi {} e o menor foi {}!'.format(cont, media, maior, menor))

# Guanabara fez igual
