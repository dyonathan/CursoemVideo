# Calcular o IMC de uma pessoa

peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))

imc = peso / (altura ** 2)

print('Seu IMC (índice de massa corporal) é {:.2f} !'.format(imc))

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
