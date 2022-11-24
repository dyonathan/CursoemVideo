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



