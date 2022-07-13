
"""quando se coloca as tres aspas no print ele mostra o texto com enter, uma aspas somente mostraria a primeira linha
print('''Lorem Ipsum is simply dummy text of the printing and
typesetting industry. Lorem Ipsum has been the industry's standard 
dummy text ever since the 1500s, when an unknown printer took a 
galley of type and scrambled it to make a type specimen book. It has
 survived not only five centuries, but also the leap into electronic
  typesetting, remaining essentially unchanged. It was popularised in
   the 1960s with the release of Letraset sheets containing Lorem
    Ipsum passages, and more recently with desktop publishing
     software like Aldus PageMaker including versions of Lorem
      Ipsum.''') """

frase = 'Curso em Vídeo Python'

''' Passa a frase para maiusulo e conta quandos O maiusculos tem na frase ou seja 3 '''
'''print(frase.upper().count('O'))'''

'''frase = '   Curso em Vídeo Python'''
''' Conta quantos caracteres tem na string frase vai dar 24 por causa dos 3 espaços no inicio da string'''
'''print(len(frase))'''
''' Retira os espaços desnecesarios do inicio e do final e conta quantos caracteres tem na string '''
'''print(len(frase.strip()))'''

''' Troca a palavra Python por Android somante na hora de mostrar esse print em especifico '''
'''print(frase.replace('Python', 'Android'))'''
''' Troca permanentemente a palavra python pela palavra android '''
'''frase = frase.replace('Python', 'Android')'''

''' Divide a string frase em varias listas separadas pelo espaço '''
dividido = frase.split()
''' mostra a lista dividido '''
'''print(dividido)'''
''' mostra o primeiro string da lista dividido ou seja Curso'''
'''print(dividido[0])'''
'''mostra a terceira letra da segunda string ou seja e'''
'''print(dividido[2][3])'''

