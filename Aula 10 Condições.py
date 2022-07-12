# se e se não

# programa que lé a idade de um carro e fala se ele tem mais ou menos de 3 anos

'''
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')

# Fazendo o if com condição simplificada, como se fosse um operador ternário

tempo = int(input('Quantos anos tem seu carro? '))
print('Carro novo' if tempo <= 3 else 'Carro velho')
print('--FIM--')
'''

# Ver se seu nome é gustavo

'''
nome = str(input('Qual é seu nome? ')).strip().lower()
if nome == 'gustavo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}'.format(nome).title())
'''

# Ver se a nota média é boa ou ruim
'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

# if simplificado

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
print('PARABÉNS' if m >= 6.0 else 'ESTuDE MAIS!')
'''
