#Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

num = int(input('Digite um valor: '))

dobro = num * 2
triplo =  num * 3
raiz = num **(1/2)

print('o valor {} possui como dobro {}, triplo como {} e a raiz quadrada como {}'.format(num,dobro,triplo,raiz))