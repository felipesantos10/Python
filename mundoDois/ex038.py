num1 = int(input('informe um numero: '))
num2 = int(input('informe outro numero: '))
if  num1 > num2:
    print('O primeiro numero {} é maior'.format(num1))
elif num2 > num1:
    print('O segundo numero {} é maior'.format(num2))
elif num1 == num2:
    print( 'OS NUMEROS SÃO IGUAIS')