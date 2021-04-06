#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dolares ela pode comprar
#considere = RS3.27

real = float(input('Quantos reais você possui? '))
dolares = real/3.27

print('Com {} reais é possivel comprar U${:.2f}'.format(real,dolares))