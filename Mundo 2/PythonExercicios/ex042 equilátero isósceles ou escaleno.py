# Ver se forma um triangulo, se formar, ver se é equilátero, isósceles ou escaleno
'''
l1 = float(input('Qual o primeiro lado? '))
l2 = float(input('Qual o segundo lado? '))
l3 = float(input('Qual o terceiro lado? '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    if l1 != l2 and l1 != l3 and l2 != l3:
        print('Forma um triângulo escaleno!')
    elif l1 == l2 and l1 == l3 and l2 == l3:
        print('Forma um triângulo equilátero!')
    else:
        print('Forma um triângulo isósceles!')
else:
    print('Não forma um triângulo!')
'''

# Guanabara fez

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILATERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
