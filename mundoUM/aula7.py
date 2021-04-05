#Nessa aula, vamos aprender quais são os operadores aritméticos do Python e também sua ordem de precedência dentro de expressões matemáticas. Veja como funcionam os operadores de adição, subtração, multiplicação, divisão, exponenciação e quociente na linguagem Python.adores

#  + adição
#  - subtração
#  * multiplicação
#  / divisão
#  **pontenciação
#  // divisão inteira
#  */* resto da divisão
#  numero**(1/2) raiz quadrada

#Ordem de precedência
#1 ()
#2 **
#3 *, /, //, */*
#4 + , -

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1 + n2
multiplicacao = n1 * n2
subtracao = n1 - n2
divisao = n1/n2
print('a soma é {}, o produto {}, subtração{} e a divisão{:.3f}'.format(soma,multiplicacao,subtracao,divisao)) 
