#Escreva um programa que leia um valor em metros e o exiba convertdo em centimentros e milimetros

metros = float(input('Digite o valor: '))
centimetro = metros * 100
milimetros = metros * 1000

print('O {} metros equivale a {} centimetros e {} milimetros'.format(metros,centimetro,milimetros))