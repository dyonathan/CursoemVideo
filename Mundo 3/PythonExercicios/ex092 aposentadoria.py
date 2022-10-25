#Ler o nome, ano de nascimento e carteira de trabalho, mas cadastrar a idade e não o nascimento
#se CTPS diferente de zero cadastrar o ano de contratação e o salário
#mostrar idade e ano de aposentadoria
'''
from datetime import date

pessoa = {}

pessoa['nome'] = str(input('Nome: '))
nasc = int(input('Ano Nascimento: '))
hj = date.today()
idade = hj.year - nasc
pessoa['idade'] = idade

while True:
    pessoa['ctps'] = int(input('Número da carteira de trabalho (0 não tem): '))
    if pessoa['ctps'] == 0:
        break
    else:
        pessoa['contratacao'] = int(input('Ano de contratação: '))
        pessoa['salario'] = float(input('Salário: R$ '))
        apos = pessoa['contratacao'] - nasc + 35
        pessoa['aposentadoria'] = apos
        break

print('-=' * 30)
print(pessoa)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')

'''
#Guanabara fez

from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valo {v}')

