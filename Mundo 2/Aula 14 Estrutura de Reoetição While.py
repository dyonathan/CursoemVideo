# o while e o for podem ser usados quando se sabe o limite de vezes que é para repetir algo, se você não souber o limite, deve se usar o while

# Mesmo programinha em for e em while
'''
for c in range(1, 10):
    print(c)
print('Fim')
'''

'''
c = 1
while c < 10:
    print(c)
    c += 1 # Mesmo que c = c + 1, somente no python tem esse +=
print('Fim')
'''

# Exemplo de programa que é necessário o while
'''
n = 1
while n != 0: # Só vai para de pedir valores quando o usuário digitar 0
    n = int(input('Digite um valor: '))
print('Fim')
'''

# Outro exemplo perguntando se quer ou não continuar
'''
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
print('Fim')
'''

# contar n números e ver se eles são impares ou pares
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números impares!'.format(par, impar))
