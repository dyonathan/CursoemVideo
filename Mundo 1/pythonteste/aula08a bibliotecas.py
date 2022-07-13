""" o import math importa toda a biblioteca de matematica
    O from math import sqrt importa somente a função sqrt da biblioteca de matematica
    pode colocar mais funções com a separação da virgula from math import sqrt, floor"""

from math import sqrt, floor

num = int(input('Digite um numero: '))

""" Se importar toda a biblioteca (import math) precisa colocar 
    raiz = biblioteca.função(variável) ou seja raiz = math.sqrt(num)
    Se importar a função direta (from math import sqrt) ficaria assim
    raiz = função(variável) ou seja raiz = sqrt(num)"""

raiz = sqrt(num)

""" para arredondar para cima usa o math.ceil(raiz) para arredondar para baixo math.floor(raiz) 
 o {:.2f} deixa somente duas casas decimais """

print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))
