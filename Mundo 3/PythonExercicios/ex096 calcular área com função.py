#Criar uma função chamada área()
#ler largura e compimento
#mostrar área do terreno


def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {a}m².')


print('Controle de Terrenos')
print('-' * 20)
area(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))
