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

#EX:
def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)

titulo('   CURSO EM VÍDEO   ')
titulo('  PYTHON É MUITO BOM  ')
'''

#Aula pratica

#Exemplo matemático
'''
a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 1
b = 2
s = a + b
print(s)
'''
#Posso substituir por:
'''
def soma(a, b):
    s = a + b
    print(s)


soma(4, 5)
soma(8, 9)
soma(1, 2)

#se eu passar 1 ou 3 numeros como parâmetros(entre parenteses) o programa dá erro

soma(4)
soma(1, 3, 6)


#Posso também especificar qual é a e qual é b
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B é {s}')

soma(b=4, a=5)
#se definir somente uma das variáveis dá errado
#soma(b=4, 5)
'''

#Empacotador e desempacotar
#O empacotador consegue pegar n numeros de parametro, oque dava erro no caso passado
#sem empacotador, para funcionar usa o * e o parametro

#Mostra os números de cada parametro
'''
def contador(* num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM')

#Conta quantos números tem em cada parametro
def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
'''

#Criando funções com listas e não com tuplas

#Dobra os valores dado na lista valores
'''
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
'''

#Função com lista é desempacotamento

#Resolvendo o problema da soma la do começo da aula de vários números
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)
