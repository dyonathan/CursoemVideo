#Criar uma função chamada área()
#ler largura e compimento
#mostrar área do terreno

'''
def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {a}m².')


print('Controle de Terrenos')
print('-' * 20)
area(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))
'''
#Guanabara fez


def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')

# Programa principal
print(' Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
