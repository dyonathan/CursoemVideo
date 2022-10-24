#Ler nome e média e mostrar nome média e situação de cada aluno
'''
aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
print('-=' * 30)
print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]}')
if aluno["media"] >= 7:
    print('Situação é igual a Aprovado!')
elif aluno["media"] >= 5 and aluno["media"] < 7:
    print('Situação é igual a Recuperação!')
else:
    print('Situação é igual a Reprovado!')
'''

#Guanabara fez

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')
