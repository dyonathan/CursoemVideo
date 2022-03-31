# Ler um salário e aumentar 15%

s = float(input('Qual o salario atual? '))
ns = s * 1.15
print('R$ {} com o aumento de 15% fica R$ {:.2f}'.format(s, ns))
