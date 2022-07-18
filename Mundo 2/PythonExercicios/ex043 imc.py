# Calcular o IMC de uma pessoa
'''
peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))

imc = peso / (altura ** 2)

print('Seu IMC (índice de massa corporal) é {:.1f} !'.format(imc))

if imc < 18.5:
    print('Abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal!')
elif imc >= 25 and imc < 30:
    print('Sobrepeso!')
elif imc >= 30 and imc < 40:
    print('Obesidade!')
else:
    print('Obesidade mórbida!')
'''

# Guanabara fez

peso = float(input('Qual é seu peso? (kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal!')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO!')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
elif imc >= 40:
    print('Você está em OBESIDADE MORBIDA, cuidado!')
