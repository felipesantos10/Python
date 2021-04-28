#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
km = int(input('Qual a distancia percorrida? '))

if km <= 200:
    preço = km * 0.50
    print('O valor da passagem é {}R$'.format(preço))
else:
    preço = km * 0.45
    print('o valor da passagem será {}R$'.format(preço))