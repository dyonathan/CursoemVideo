# Ler duas notas e fazer média, se menor que 5 reprovado, até 6.9 recuperação ou maior aprovado

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
