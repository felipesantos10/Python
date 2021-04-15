#Utilizando módulos
#import math ( importando toda a biblioteca de matematica)
#from math import sin( importante apenas as informações que eu necessito da biblioteca)

#funcionalidades do match
#Funcionalidade do match
#ceil (arrendomamento pra cima)
#floor (arredodamento pra baixo)
#trunc ( quebrar o numero)
#pow (potencia)
#sqrt (raiz quadrada)
#factorial (calculo fatorial)

#Primeiro forma
import math
num = int(input('Digite um numero? '))
raiz = math.sqrt(num)

print('A raiz do numero {} é igual a  {}'.format(num,raiz))

#Segunda forma
from math import sqrt
num = int(input('Digite um numero? '))
raiz = sqrt(num)

print('A raiz do numero {} é igual a  {}'.format(num,raiz))



