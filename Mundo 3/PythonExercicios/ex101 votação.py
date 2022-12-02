#Criar uma função chamada voto() que receba o ano de nascimento
#Retornar Negado, Opcional ou Obrigatório
'''
from datetime import date


def voto(nasc):
    print('-' * 30)
    ano = date.today().year
    idade = ano - nasc
    if idade < 16:
        votar = 'NÃO VOTA.'
    elif idade >= 16 and idade < 18 or idade > 65:
        votar = 'VOTO OPCIONAL.'
    else:
        votar = 'VOTO OBRIGATÓRIO.'
    print(f'{idade} anos: {votar}')


voto(nasc=int(input('Em que ano você nasceu? ')))
'''


#Guanabara fez


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 18:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO.'

# Programa principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
