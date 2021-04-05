#Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e antecessor.

num = int(input('Digite um número: '))

ant = num - 1
suc = num + 1

print('O número {} possui como sucessor {} e antecessor {}'.format(num,suc,ant))