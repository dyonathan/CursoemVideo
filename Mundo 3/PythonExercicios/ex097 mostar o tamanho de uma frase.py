#Fazer uma função chamada escreva()
#lêr uma frase
#mostar uma mensagem com tamanho adaptável.
#Ex:
#escreva('Olá, Mundo!')
#mostrar:
#~~~~~~~~~~~~~~~
#  Olá, Mundo!
#~~~~~~~~~~~~~~~
#Ex 2:
#~~~~~~~~
#  Casa
#~~~~~~~~
'''
def escreva(msg):
    print(f'{"~"}' * (len(msg) + 4))
    print(f'  {msg}')
    print(f'{"~"}' * (len(msg) + 4))


escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')
'''
#Guanabara fez


def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# Programa principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')
