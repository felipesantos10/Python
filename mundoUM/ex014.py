#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

print('---Conversor de temperatura---')

celsius = float(input('informe a temperatura em graus celsius? '))
fahrenheit = (celsius * 1.8) + 32

print('a temperatura de {}°C equivale a {:.2f}°F'.format(celsius,fahrenheit))