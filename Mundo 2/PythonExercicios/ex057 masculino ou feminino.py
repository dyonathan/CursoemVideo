# só aceitar se o sexo ou m para masculino ou f para feminino

sexo = ''
while sexo != 'f' and sexo != 'm':
    sexo = str(input('Qual o sexo[M/F]: ').lower())
    if sexo != 'f' and sexo != 'm':
        print('Sexo inválido, digite m para masculino ou f para feminino!')
        print(sexo)
