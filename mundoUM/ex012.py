#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

produto = float(input('Qual o preço do produto? '))
desconto = (produto *95)/100

print('Parabens, você ganhou um desconto de 5% no produto, você ira pagar apenas R${}'.format(desconto))