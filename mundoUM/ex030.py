#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Informe um numero: '))
oper = (num % 2)

if oper == 0:
    print('O numero {} é par'.format(num))
else:
    print('o numero {} é impar'.format(num))
