# formatações para nomes

nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {}!'.format(nome)) # normal
print('Prazer em te conhecer {:20}!'.format(nome)) # aparece em 20 caracteres
print('Prazer em te conhecer {:>20}!'.format(nome)) # aparece alinhado a direita
print('Prazer em te conhecer {:<20}!'.format(nome)) # alinhado a esquerda
print('Prazer em te conhecer {:^20}!'.format(nome)) # Centralizado
print('Prazer em te conhecer {:=^20}!'.format(nome)) # centralizado com igual no espaço vazio
