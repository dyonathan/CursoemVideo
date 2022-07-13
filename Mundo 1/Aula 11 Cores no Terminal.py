'''
ANSI tem escape sequence que funciona em vários ambientes mas nesse caso vamos usar para o terminal, tudo dentro de ANSI começa com contra barra \ que é o caractere de scape dentro do python do c entre outras linguagens, o codigo ANSI começa com contra-barra \ depois vem o codigo, um dos codigos para cores e existe uma faixa de codigos, mas o que funciona melhor em python é o \033[ depois você vai indicar o style do texto negrito, italico, etc. depois a cor do texto e por último a cor do fundo e no final junto com a cor do fundo coloca um m por exemplo \033[0;33;44m, todos eles são opcionais e pode ser colocado em qualquer sequencia.

os codigos do padrao ANSI 033 são

style               text                back
0 sem estilo        30 Branco           40 Branco
1 Negrito           31 Vermelho         41 Vermelho
4 Sublinhado        32 Verde            42 Verde
7 Negativo          33 Amarelo          43 Amarelo
                    34 Azul             44 Azul
                    35 Roxo             45 Roxo
                    36 Azul claro       46 Azul claro
                    37 Cinza            47 Cinza

'''

# TESTES

\033[0;30;41m] # Letra normal, cor branca e fundo vermelho
\033[4;33;44m] # Letra sublinhada, cor amarela e fundo azul
\033[1;35;43m] # letra negrito, cor roxo e fundo amarelo
\033[30;42m] # letra normal, cor branca e fundo verde
\033[m] # letra normal, cor cinza e fundo preto (padrão)
\033[7;30m] # letra negativo ele inverte as cores, cor branca fica preta e fundo preto fica branco

