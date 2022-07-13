'''frase = ['C','u','r','s','o',' ','e','m',' ','V','i','d','e','o',' ','P','y','t','h','o','n']'''
frase = 'Curso em Video Python'

''' FATIAMENTO, fatiar uma frase ou seja pegar somente uma parte dela '''

''' Mostra ['C', 'u', 'r', 's', 'o', ' ', 'e', 'm', ' ', 'V', 'i', 'd', 'e', 'o'] '''
'''print(frase)'''

''' Mostra o nono item da lista ou seja V'''
'''print(frase[9])'''

''' Mostra do nono até o decimo terceiro item da lista ou seja ['V', 'i', 'd', 'e', 'o']'''
'''print(frase[9:14])'''

''' Mostra do nono até o vigésimo item pulando de 2 em 2 ou seja ['V', 'd', 'o', 'P', 't', 'o']'''
'''print(frase[9:21:2])'''

''' Mostra do inicio até o quarto item ou seja ['C', 'u', 'r', 's', 'o']'''
'''print(frase[:5])'''

''' Mostra do decimo quinto item até o final ou seja ['P', 'y', 't', 'h', 'o', 'n']'''
'''print(frase[15:])'''

''' Mostra do nono ate o ultimo item pulando de 3 em 3 ou seja ['V', 'e', 'P', 'h']'''
'''print(frase[9::3])'''

''' ANÁLISE, análisa qual o tamanho da string, qual a primeira palavra, se tem uma palavra especifica nela, etc. '''

''' len mostra o comprimento da frase nesse caso tem 21 caracteres'''
'''print(len(frase))'''

''' Conta quantas vezes a letra o minuscula aparece no texto no caso 3'''
'''print(frase.count('o'))'''
''' era para contar quantas letras o tem do 0 até o 12 mas está dando argumento invalido '''
'''print(frase.count('o', 0, 13))'''

'''mostra em qual posição inicia a frase deo'''
'''print(frase.count('deo'))'''
''' Na frase não tem escrito android então retorna -1 quando a string não existe no texto retorna -1'''
'''print(frase.find('Android'))'''

''' Fala se existe a string dentro a lista frase e retorna true ou false'''
'''print('C', 'u', 'r', 's', 'o' in frase)'''


''' TRANSFORMAÇÃO, a string é imutavel mas dá para mecher nela atraves de metodos '''

''' Subistituiria a string Python pela string Android'''
'''print(frase.replace('Python','Android'))'''

''' Coloca a string toda em maiuscula '''
'''print(frase.upper())'''

''' Coloca a string em minusculo'''
'''print(frase.lower())'''

''' Deixa somente a primeira letra da string em maiuscula ou seja o C do inicio'''
'''print(frase.capitalize())'''

''' Deixa a primeira letra de daca palavra da string em maiucula ou seja C E V P'''
'''print(frase.title())'''

''' Mudando a string para tratar o espaço no começo da string'''
'''frase = '   Aprenda Python  '''

''' Mostra a string normal com os espaços no começo'''
'''print(frase)'''

''' Mostra a string sem o espaço no começo '''
'''print(frase.strip())'''

''' Retira somente os espaços que estão no lado direito por isso o r no inicio da função '''
'''print(frase.rstrip())'''

''' Retira somente os espaços que estão no lado esquerdo por isso o l no inicio da função '''
'''print(frase.lstrip())'''

''' DIVISÃO, permite dividir strings '''

''' Divide uma string em varias dependendo da quantidade de espaços, ou seja sempre que ouver um espaço na string ela vira uma string nova, ou seja 'Curso em video python' vira 'curso' 'em' 'video' 'python' '''
print(frase.split())

''' JUNÇÃO,  a função split divide a stryng e a funçao join junta ela, faz o contrario '''

''' Junta a string que foi separada, ou strings que são separadas, entre as aspas coloca o caractere de separação no caso está fazia mesmo '''
print(''.join(frase))


