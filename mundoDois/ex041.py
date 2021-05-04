#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

ano = int(input('Ano de nascimento: '))
categoria = 2021 - ano
if categoria <= 9:
    print('MIRIM')
elif categoria <= 14:
    print('INFANTIL')
elif categoria <= 19:
    print('JUNIOR')
elif categoria <= 25:
    print('SÊNIOR')
else:
    print('MASTER')