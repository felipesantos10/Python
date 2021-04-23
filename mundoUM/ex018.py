3#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
ang = float (input('Valor do angulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print('O angulo {} apresenta seno de {:.2f} cosseno de {:.2f} e tangente igual a {:.2f}'.format(ang,sen,cos,tan))
