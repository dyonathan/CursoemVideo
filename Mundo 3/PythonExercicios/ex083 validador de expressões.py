# ler expressão que use parenteses, olhar se os parenteses estão corretos
#Não consegui fazer
'''
expressao = list()

asd = str(input('Fale uma expressão aritmetica: ')).strip().lower()
sequencia = asd.split()

for c in range(0, len(sequencia)):
    print('(' in sequencia)
    print(')' in sequencia)


print(sequencia)
print(len(sequencia))
'''

#Guanabara fez

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está valida!')
else:
    print('Sua expressão está errada!')

