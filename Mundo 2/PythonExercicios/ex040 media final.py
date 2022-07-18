# Ler duas notas e fazer média, se menor que 5 reprovado, até 6.9 recuperação ou maior aprovado
'''
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

m = (n1 + n2)/2

print('Sua média foi {:.1f}'.format(m))
if m < 5:
    print('Reprovado')
elif m > 5 and m < 7:
    print('Recuperação')
else:
    print('Aprovado')
'''

# Guanabara fez

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
if 7 > media >= 5:
    print('O aluno está em RECUPERAÇÃO.')
elif media < 5:
    print('O aluno está REPROVADO.')
else:
    print('O aluno está APROVADO.')
