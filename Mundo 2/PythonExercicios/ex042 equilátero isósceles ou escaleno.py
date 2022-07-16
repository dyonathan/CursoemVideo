# Ver se forma um triangulo, se formar, ver se é equilátero, isósceles ou escaleno

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
