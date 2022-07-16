# Programa para aprovar empréstimo bancário, perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar, calcular mensalidade se ela exceder 30% do salário empréstimo negado

print('Se a mensalidade for maior que 30% do salário o emprestimo vai ser negado!')
casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário? R$ '))
anos = int(input('Pagar em quantos anos? '))

meses = anos * 12
mensalidade = casa / meses

print('Você vai pagar R$ {:.2f} por mês, 30% do seu salário é {}.'.format(mensalidade, salario * 0.3))

if mensalidade >= salario * 0.3:
    print('Seu empréstimo não foi aprovado!')
else:
    print('Empréstimo aprovado!')
