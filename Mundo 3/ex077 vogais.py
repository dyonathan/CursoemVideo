# Fazer uma tupla com várias palavras (sem acento) e mostrar as vogais das palavras

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')


for c in range(0, len(palavras)):

    vogais = str.split(palavras[c])

    print(f'Na palavra {palavras[c]} temos ', end=' ')
    for d in range(0, len(vogais)):
        if 'a' in vogais[d]:
            print('a', end=' ')
        if 'e' in vogais[d]:
            print('e', end=' ')
        if 'i' in vogais[d]:
            print('i', end=' ')
        if 'o' in vogais[d]:
            print('o', end=' ')
        if 'u' in vogais[d]:
            print('u', end=' ')
    print('')