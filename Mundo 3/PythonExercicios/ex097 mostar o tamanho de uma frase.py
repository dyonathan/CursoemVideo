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

def separador(msg):
    print('~' * len(msg))
    print(msg)
    print('~' * len(msg))


separador('  Gustavo Guanabara  ')
separador('  Curso de Python no YouTube  ')
separador('  CeV  ')
