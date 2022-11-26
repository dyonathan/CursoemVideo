#Como utilizar a ajuda interativa

#no console, digite help()
#depois digite o comando que você quer ajuda por exemplo o print depois vai aparece
#um texto falando oque aquela função faz para sair digite quit

#outra maneira é fazer direto no programa por exemplo
#help(print) ele vai aparecer no run oque faz o print

#print(input.__doc__) mostra oque faz o input

#Docstrings

#Uma docstring é uma string de documentação como foi feito ai em cima
'''
def contador(i, f, p):
    """
     -> Faz uma contagem e mostra na tela.
     :param i: início da contagem
     :param f: fim da contagem
     :param p: passo da contagem
     :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')


contador(2, 10, 2)

#Logo apos a def entre os 3 parenteses coloca o texto para falar oque a função faz
#esse texto que aparece no help do def ou seja o docstring do contador

help(contador)

'''
#Parâmetros opcionais

'''
def somar(a=0, b=0, c=0):#A letra = 0 significa que se não passar valor ele vale 0
    """
     -> Faz a soma de três valores e mostra o resultado na tela
     :param a: o primeiro valor
     :param b: o segundo valor
     :param c: o terceiro valor
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
'''

#Escopo de variáveis


#Exemplo de escopo global
'''
def teste():
    print(f'Na função teste n vale {n}')

#Programa principal
n = 2
print(f'No programa principal, n vale {n}')
teste()
'''

#Primeiro mostra o programa principal, depois o teste chama a def
#mesmo o n sendo definido no programa principal ele vale para todo o programa,
#isso é chamado de variavel global

'''
def teste():
    x = 8
    print(f'Na função teste n vale {n}')
    print(f'Na função teste n vale {x}')

#Programa principal
n = 2
print(f'No programa principal, n vale {n}')
teste()
print(f'No programa principal, n vale {x}')
'''

#O x funciona somente dentro de teste no programa principal ele da erro,
#isso porque ele só existe dentro de teste isso é chamado de variavel local

#Outro exemplo

'''
#Versão 1
def teste(b):
    #Escopo local
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')
    #b e c só exitem dentro do teste, são variáveis locais
    #b vale 9 e c vale 2 porque 5 do a global mais 4 do b local


#Escopo global
a = 5
teste(a)
print(f'A fora vale {a}')
#Se colocar print b e c vai dar erro, porque eles só existem lá dentro do teste
'''


'''
#Versão 2
def teste(b):
    #Escopo local
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    #Antes o a dentro valia 5 porque como não tinha a variável a local, ele usava o global, más
    #como agora temos o a local o A dentro passa a valer 8 que é o valor local
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')
    #b e c só exitem dentro do teste, são variáveis locais
    #b vale 9 e c vale 2 porque 5 do a global mais 4 do b local


#Escopo global
a = 5
teste(a)
print(f'A fora vale {a}')
#Se colocar print b e c vai dar erro, porque eles só existem lá dentro do teste
'''


'''
#Versão 3
def teste(b):
    #Escopo local
    global a
    #A função global a, faz com que o a local mude o a global, antes ele  valia 5 agora vale 8
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')
    #b e c só exitem dentro do teste, são variáveis locais
    #b vale 9 e c vale 2 porque 5 do a global mais 4 do b local


#Escopo global
a = 5
teste(a)
print(f'A fora vale {a}')
#Se colocar print b e c vai dar erro, porque eles só existem lá dentro do teste
'''


#Retorno de valores (return)


'''
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Os resultados foram {r1}, {r2} e {r3}.')
'''


#Aula pratica


'''
#Versão 1
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


#mostra somente o resultado de uma conta por vez 
n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
'''


'''
#Versão 2
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


#Mostra o resultado de várias contas
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')
'''


#A função return pode retornar outros tipos de dados alem de números


'''
#Versão 1
def par(n=0):
    if num % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
print(par(num))
'''


#Versão 2
def par(n=0):
    if num % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):#Funcionou porque para definir o if usa True ou False por resultado de comparação aqui já foi direto
    print('É par!')
else:
    print('Não é par!')

