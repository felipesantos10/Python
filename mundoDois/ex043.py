peso = float(input('Qual o seu peso atual? '))
altura = float(input('Qual a sua altura? '))
imc = peso /(altura**2)

if imc < 18.5:
    print('seu imc é de {:.1f} , você se encontra ABAIXO DO PESO'.format(imc))
elif  imc >= 18.5 and imc < 25:
    print(  'seu imc é de {:.1f} , você se encontra PESO IDEAL'.format(imc))
elif imc > 25  and imc < 30:
    print('seu imc é de {:.1f} , você se encontra SOBREPESO'.format(imc))
elif imc >= 30 and imc < 40:
    print('seu imc é de {:.1f} , você se encontra OBESIDADE'.format(imc))
else:
    print('seu imc é de {:.1f} , você se encontra OBESIDADE MORBIDA'.format(imc))
