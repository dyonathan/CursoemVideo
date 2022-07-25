# Mostrar a tabuada de n números, parar quando digitar um número negativo

print('Informe o valor para tabuada ou número negativo para sair')
num = int(input('Qual o número da tabuada? '))
produto = 0

while True:

    if num < 0:
        break

    for produto in range(0, 11):
        total = num * produto
        print(f'{num} x {produto:2} = {total}')
        produto += 1

    print('Informe o valor para tabuada ou número negativo para sair')
    num = int(input('Qual o número da tabuada? '))

print('Até mais!')
