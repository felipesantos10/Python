#Desenvolva um programa que leia as duas notas de um aluno,calcule e mostre a sua media.

nome = input('Qual o seu nome? ')
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1+n2)/2
print(' O aluno {} obteve a media {:.2f}'.format(nome,media))