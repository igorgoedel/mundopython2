#Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
#tentar advinhar até acertar, mostrando no final quantos palpites foram necessarios para vencer.
from random import randint
computador = randint(0, 10)
print('Sou o seu computador..')
print('Pensei em um número entre 0 e 10 tnete advinhar qual númeor eu pensei..')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite ?'))
    if jogador == computador:
        print('Parabêns você acertou!')
        acertou = True
    elif jogador < computador:
        print('Mais..')
        palpite += 1
    elif jogador > computador:
        print('Menos..')
        palpite += 1
print('Você jogou {} e o computador {}, você acertou seu palpite depois de {} jogadas.'.format(jogador, computador, palpite))

#Jeito do professor
from random import randint
computador = randint(0,10)#Aqui ele não ignora o ultimo número ele realmente conta de 0 a 10.
print('Eu sou o seu computador... acabei de pensar em um número entre 0 e 10.')
print('Será que você concegue adivinhar? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite ?'))
    palpites += 1#Vai somar mais um quando o jogador jogar.
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou!, com {} tentativas, Parabêns!'.format(palpites))
