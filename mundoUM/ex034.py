#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual o seu salario atual? '))

if salario >1250:
    aumento = salario + (salario * 10/100)
    print('O seu salario recebeu um aumento de 10%, passou a ser {}'.format(aumento))

if salario <= 1250:
    aumento = salario + (salario * 15/100)
    print('O seu salario recebeu aumento de 15%, passou a ser {}'.format(aumento))