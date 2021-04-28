#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input('Em que ano você está? '))

bis = ano%4
if bis == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))