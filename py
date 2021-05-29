from random import randint

restart = True

while restart:

    limite = 0
    acertou = True
    fase = 1
    totalp = 0
    record = 0

    print('Digite seu Nickname ')                               
    nick = str(input())
    print('Bem vindo Jogador ', nick, '!')

    while acertou:                                              
        limite += 10
        computador = randint(0, limite)

        print('FASE', fase, )
        print(f'Acabei de pensar em um número entre 0 e {limite}.')
        print('Será que você consegue adivinhar qual foi? ')

        acertou = False
        palpites = 0
        jogador = 0

        while not acertou and (palpites < 10):              
            palpites += 1
            correto = False

            while not correto:                                  
                try:
                    jogador = int(input('Qual o seu palpite? '))
                    correto = True
                except:
                    print('Por favor informe um número válido')
                    correto = False

            if jogador == computador:
                fase += 1
                acertou = True
            else:
                if jogador < computador:
                    print('Mais... Tente mais uma vez')
                elif jogador > computador:
                    print('Menos... Tente mais uma vez')

        pontos = (10 - palpites)                                

        if palpites < 10:
            totalp += pontos
            print('Você acertou com', palpites, 'palpites')
            print('Seus pontos são:', pontos)
            print('Você terminou com ', totalp, 'pontos e chegou na fase ', fase, '\U0001F603')

        if palpites >= 10:
            totalp += pontos
            print('Você perdeu com ', pontos, 'pontos')

            if totalp > record:                                
                record += totalp
            print('Seu record é ', record, )
            print('Quer jogar novamente? Y ou N')

            correto2 = False

            cond = str(input())

            if cond == 'y':
                restart = True
            else:
                restart = False
                print('Obrigado por Jogar', '\U0001F609', )
