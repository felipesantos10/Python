#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la,sabendo que cada litro de tinta pinta uma area de 2m

largura = float(input("Qual a largura da parede? "))
altura = float(input("Qual a altura da parede? "))
area = largura * altura
tinta = area/2

print('A area da parede é {} para pinta-la sera necessario {}L de tinta'.format(area,tinta))