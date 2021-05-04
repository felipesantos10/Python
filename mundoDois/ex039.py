#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

nome = str(input("Qual o seu nome soldado? "))
ano = int(input("Em que ano você nasceu? "))

militar = 2021 - ano

if militar < 18:
    print('Soldado {}! Você está prestes a se alistar!'.format(nome))

elif militar == 18:
    print( "Soldado {}! É hora de se alistar ao serviço militar".format(nome))
elif militar > 18:
    print( 'SOLDADO {}! Voce não pode mais se alistar!'.format(nome))