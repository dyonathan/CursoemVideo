# Ver se um número é primo

# inicializa a variável s
s = 0
n = int(input('Digite um número: '))

# coloca n + 1 porque ele conta somente até o número antes de n
for c in range(1, n + 1):
    if n % c == 0:
        s += 1
# 2 porque tem que dividir por 1 e ele mesmo
if s != 2:
    print('Não é um número primo!')
else:
    print('É um número primo!')

