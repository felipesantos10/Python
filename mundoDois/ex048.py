#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
s = 0
for impar in range(1,500,2):
    if impar % 3 ==0:
        print(impar)
        s = s+impar
print('o somatorio de todos os valores impar foi {}'.format(s))

