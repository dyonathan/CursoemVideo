#Cadastrar n alunos e duas notas para cada aluno
#no final mostrar
#um tabela com o numero nome e média escolar para cada aluno
#ex:
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#No. NOME        MÉDIA
#---------------------------
#0   Maria       7.5
#1   Claudio     2.8
#2   Ana         10.0
#---------------------------

#depois perguntar se quer ver algum aluno especifico ou digitar 999 para sair do programa
#se escolher o numero de um aluno, mostrar
#nome e as notas que ele tirou

dado = []
aluno = []
media = []
nota = []
temp = []

while True:

    nome = str(input('Nome do aluno: '))
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    op = str(input('Quer continuar? '))
    m = (temp[0] + temp[1]) / 2
    aluno.append(nome)
    media.append(m)
    nota.append(temp[:])
    temp.clear()
    if op in 'Nn':
        break

print('-=' * 20)
print('No. NOME        MÉDIA')
print('-' * 30)
#for c, v in enumerate:
for c in range(0, len(aluno)):
    print(c, end='   ')
    print(aluno[c], end='         ')
    print(media[c])
print('-' * 30)

while True:
    cont = int(input('Quer ver as notas de algum aluno ou 999 para sair: '))
    if cont == 999:
        break
    print(f'Notas de {aluno[cont]} são {nota[cont]}')
