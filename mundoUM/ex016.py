#Crie um programa que leia um numero na Real qualquer pelo teclado e mostre na tela a sua porção inteira.

#Metodo 1
import math
num = float(input("Digite um valor:  "))
real = math.trunc(num)
print('O valor digitado foi {:.3f} e sua porção inteira é {}'.format(num,real))

#Metodo 2
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num,trunc(num)))
