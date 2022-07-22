# só aceitar se o sexo ou m para masculino ou f para feminino
'''
sexo = ''
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Qual o sexo[M/F]: ').upper())
    if sexo != 'F' and sexo != 'M':
        print('Sexo inválido, digite m para masculino ou f para feminino!')

print('Sexo {} registrado com sucesso!'.format(sexo))
'''

# Guanabara fez

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0] # esse 0 no final é para pegar somente a primeira letra
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
