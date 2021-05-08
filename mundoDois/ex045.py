#Crie um programa que faça o computador jogar Jokenpô com você.


inicio = str(input('''Bem vindo ao jokenpô!!!
Vamos começar? sim/não  
'''))
if  inicio == 'sim':
    import random
    from time import sleep

    itens = ( 'pedra','papel','tesoura')
    maquina = random.randint(0,2)

    humano = int(input('''Escolha entre
    [0]  pedra
    [1]  papel
    [2]  tesoura
    Qua a sua opção?   ''' ))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(1)
    #resposta do usuario
    print('=*='*20)
    print('Você jogou {}'.format(itens[humano]))    
    print('A maquina jogou {}'.format(itens[maquina]))
    print('=*='*20)

    if humano == 0:
        if maquina == 0:
            print('EMPATE')
        elif maquina == 1:
            print('COMPUTADOR VENCEU')
        else:
            print('VOCÊ VENCEU')

    elif  humano == 1:
        if maquina == 0:
            print('VOCE VENCEU')
        elif maquina == 1:
            print('EMPATE')
        else:
            print('COMPUTADOR VENCEU')

    elif  humano == 2:
        if maquina == 0:
            print('COMPUTADOR VENCEU')
        elif maquina == 1:
            print('VOCÊ VENCEU')
        else: 
            print('EMPATE')


else:
    print('Tudo bem, aguardo você na proxima rodada!')
