#Cria funções para coisas que fazmos constantemente
#ex:
#print(), len(), input(), int(), float()...

#Por exemplo
'''
print('-------------------------------')
print('       SISTEMA DE ALUNOS       ')
print('-------------------------------')
print('-------------------------------')
print('   CADASTRO DE FUNCIONÁRIOS    ')
print('-------------------------------')
print('-------------------------------')
print('         ERRO DO SISTEMA       ')
print('-------------------------------')

#Como repete o ------------- varias vezes pode-se subistituir por uma função

def mostralinha():
    print('-------------------------------')

#O mostralinha substitui as linhas no codigo

mostralinha()
print('       SISTEMA DE ALUNOS       ')
mostralinha()
mostralinha()
print('   CADASTRO DE FUNCIONÁRIOS    ')
mostralinha()
mostralinha()
print('         ERRO DO SISTEMA       ')
mostralinha()


#subistituir blocos iguais

def mensagem(msg):
    print('-------------------------------')
    print(msg)
    print('-------------------------------')

mensagem('SISTEMA DE ALUNOS')
'''

#EX:
def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)

titulo('   CURSO EM VÍDEO   ')
titulo('  PYTHON É MUITO BOM  ')


