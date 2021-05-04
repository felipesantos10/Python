#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

print("##### Conversor de bases Numéricas #####")
print('--'*25)
num = int(input("Escreva um numero qualquer? "))
print('''Escolha umas das bases para conversão:
[1] converter para Binario
[2] converter para OCTAL
[3] converter para HEXADECIMAL
''')
opção = int(input('Sua opção: '))

if opção == 1:
    print('{} para BINARIO é igual a {}'.format(num,bin(num)))
elif opção == 2:
    print('{} para OCTAL é igual a {}'.format(num,oct(num)))
else:
    print('{} para HEXADECIMAL é igual a {}'.format(num,hex(num)))