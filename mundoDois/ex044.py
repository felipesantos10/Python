#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto

# – à vista no cartão: 5% de desconto

# – em até 2x no cartão: preço formal 

# – 3x ou mais no cartão: 20% de juros#

print('GERENCIANDOR DE PAGAMENTO')
print('----'*15)
preço = float(input('Qual o preço do produto? '))
pagamento = str(input('''Possuimos 4 forma de pagamento
[1] dinheiro
[2] cartão
[3] duas vezes no cartão
[4] três vezes no cartão

Qual forma de pagamento você deseja utilizar?
'''))
if pagamento == '1':
    print('você selecionou a opção DINHEIRO')
    pagar = preço - (preço * 10)/100
    print('A sua compra foi no valor de {}'.format(preço))
    print( 'Você recebeu um desconto de 10%. O valor do produto ficou em {}R$'.format(pagar))

elif pagamento == '2':
    print('você selecionou a opção CARTÃO')
    pagar = preço - (preço * 5)/100
    print('A sua compra foi no valor de {}'.format(preço))
    print( 'Você recebeu um desconto de 5%. O valor do produto ficou em {}R$'.format(pagar))

elif pagamento == '3':
    print('você selecionou a opção DUAS VEZES NO CARTÃO')
    parcela = preço/2
    print('A sua compra foi no valor de {}'.format(preço))
    print( 'parcelada em 2 vezes, o preço sera de cada parcela será {}R$'.format(preço))
    
else:
    print('você selecionou a opção TRÊS VEZES NO CARTÃO')
    parcela = preço + (preço * 20/100)
    pagar = parcela /3
    print('A sua compra foi no valor de {}'.format(preço))
    print( 'O valor do produto teve 20% de juros ficou em {}R$ cada parcela ficou no total de {}'.format(parcela, pagar))