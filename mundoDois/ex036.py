#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

#dados de entrada.
print('*****EMPRESTIMO******')

casa = float(input('Informe o valor da casa? '))
salario = float(input('Qual o seu salario atualmente? '))
anos = int(input('Em quantos anos deseja pagar? '))

#prestação mensal da casa.
mensal = casa/(anos *12)
print( 'Para pagar a casa de R${:.2f} em {} anos, a prestação será no valor de {:.2f}'.format(casa,anos,mensal))
limite = (salario *30)/100

#condição aninhadas
if mensal <= limite:
    print('EMPRESTIMO FOI APROVADO')
elif mensal > limite:
    print('SEU EMPRESTIMO FOI NEGADO')
    print('a prestação mensal {:.2f}R$ foi acima dos 30% do seu salario {:.2f}R$'.format(mensal,limite))
else:
    print('até a proxima!')

