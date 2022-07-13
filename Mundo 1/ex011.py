# Calcular area de uma parede e mostrar quanta tinta precisa para pintar sabendo que 1 litro de tinda = 2m²

a = float(input('Informe a altura da parede: '))
l = float(input('Informe a largura da parede: '))
ar = a * l
t = ar / 2
print('A parede de altura {} e largura {} tem a área de {} e gasta {} litros de tinta!'.format(a, l, ar, t))
