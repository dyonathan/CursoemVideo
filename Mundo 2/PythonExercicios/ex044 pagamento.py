# ver forma de pagamento, dinheiro ou cheque 10% de desconto, debito 5% de desconto, 2x sem desconto, 3x ou mais 20% de juros

preco = float(input('Qual o valor da compra? R$ '))
op = int(input('''Qual a forma de pagamento:
1 - No dinheiro ou cheque, 10% de desconto!
2 - Débito, 5% de desconto!
3 - Crédito 2x sem desconto!
4 - Crédito 3x ou mais, 20% de juros!
Qual a opção: '''))

if op == 1:
    print('R$ {:.2f} no dinheiro ou no cheque fica R$ {:.2f} !'.format(preco, preco * 0.9))
elif op == 2:
    print('R$ {:.2f} no débito fica R$ {:.2f} '.format(preco, preco * 0.95))
elif op == 3:
    print('R$ {:.2f} em duas vezes fica, R$ {:.2f} cada parcela!'.format(preco, preco / 2))
elif op == 4:
    print('R$ {:.2f} com o juros fica, R$ {:.2f} !'.format(preco, preco * 1.2))
else:
    print('Opção invalida!')
