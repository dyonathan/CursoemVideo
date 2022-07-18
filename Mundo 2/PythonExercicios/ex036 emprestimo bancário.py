# Programa para aprovar empréstimo bancário, perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar, calcular mensalidade se ela exceder 30% do salário empréstimo negado
'''
print('Se a mensalidade for maior que 30% do salário o emprestimo vai ser negado!')
casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário? R$ '))
anos = int(input('Pagar em quantos anos? '))

# Transforma meses em anos
meses = anos * 12

# Valor da mensalidade
mensalidade = casa / meses

# Falo o valor da mensalidade e quanto dá 30% do salário
print('Você vai pagar R$ {:.2f} por mês, 30% do seu salário é {}.'.format(mensalidade, salario * 0.3))

# se 30% do salário for maior que a mensalidade, aprovado caso contrario reprovado!
if mensalidade >= salario * 0.3:
    print('Seu empréstimo não foi aprovado!')
else:
    print('Empréstimo aprovado!')
'''

# Guanabara fez

casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R$ {:.2f}.'.format(prestacao))
if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
