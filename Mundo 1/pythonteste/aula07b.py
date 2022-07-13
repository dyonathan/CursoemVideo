# operações aritméticas

n1 = int(input('Informe o primeiro numero: '))
n2 = int(input('Informe o segundo numero: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

# No colchete os : são obrigatorios, ponto para chamar a função e 3f fala que são 3 casas flutuantes
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d))
print('Divisão inteira {} e potência {}'.format(di, e))

# No final o end faz com que a segunda linha apareça no final da primeira e não embaixo
# O \n é para pular uma linha
print('\nA soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))
