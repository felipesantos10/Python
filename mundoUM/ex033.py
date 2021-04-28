#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Informe o primeiro numero: '))
n2 = int(input('Informe o segundo numero: '))
n3 = int(input('Informe o terceiro numero: '))

if n1>n2 and n1>n3:
    print('{} é o maior numero'.format(n1))
if n2>n1 and n2>n3:
    print('{} é o maior numero'.format(n2))
if n3>n1 and n3>n2:
      print('{} é o maior numero'.format(n3))
if n1<n2 and n1<n3:
    print('{} é o menor numero'.format(n1))
if n2<n1 and n2<n3:
    print('{} é o menor numero'.format(n2))
if n3<n1 and n3<n2:
    print('{} é o menor numero'.format(n3))

