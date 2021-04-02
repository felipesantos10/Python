#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input('Digite algo: ')
print('O tipo primitivo',type(a))
print('So tem espaços',a.isspace())
print('É um numero? ',a.isnumeric())
print('É alfabetico? ',a.isalpha())
