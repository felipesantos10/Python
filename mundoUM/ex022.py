#Crie um programa que lei o nome completo de uma pessoa e mostre
#O nome com todas as letras em maisculas
#O nome com todas minusculas
#Quantas letras ao todo(sem considerar os espaços vazios)
#quantas letras tem o primeiro nome

nome = str(input('Digite o seu nome completo? ')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome)-nome.count(' '))
print(nome.find(' '))
