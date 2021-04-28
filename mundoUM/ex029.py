#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
vel = int(input('Informe a velocidade do carro: '))
if vel > 80:
    limite = (vel - 80)
    multa = limite * 7
    print('Você foi multado em {}R$ por exceder o limite da rodovia.'.format(multa))
else:
    print('Não consta multa no sistema')