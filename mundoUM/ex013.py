#Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento

salario = float(input('Qual o seu salario atual? '))
aumento = (salario * 115)/100

print('Parabéns, voce obteve um aumento de 15% hein!!! Seu novo salario será R${:.2f}'.format(aumento))