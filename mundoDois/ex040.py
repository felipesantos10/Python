#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

#– Média abaixo de 5.0: REPROVADO

#– Média entre 5.0 e 6.9: RECUPERAÇÃO

#– Média 7.0 ou superior: APROVADO

num1 = float(input('Digite sua nota da prova 1: '))
num2 = float(input('Digite sua nota da prova 2: '))

media = (num1 + num2)/2

if media < 5.0:
    print('REPROVADO')
elif media >= 5.0 and media <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')