#Crie um programa que faça o computador jogar jokênpo com você.
from random import randint
computador = randint(0, 2)
print('''FAÇA A SUA ESCOLHA:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
jogador = int(input('Escolha o número correspondente ao seu jogo: '))
if jogador == 1 and computador == 0:
    print('EMPATOU!, Você e a maquina escolheram pedra.')
elif jogador == 1 and computador == 1:
    print('VOCÊ PERDEU!, o computador escolheu papel e você escolheu pedra.')
elif jogador == 1 and computador == 2:
    print('PARABÉNS VOCÊ VENCEU!, o computador escoheu tesoura e você escolheu pedra.')
elif jogador == 2 and computador == 0:
    print('PARABÉNS VOCÊ VENCEU!, o computador escolheu pedra e você escolheu papael.')
elif jogador == 2 and computador == 1:
    print('EMPATE!, você e a maquina escolheram papel.')
elif jogador == 2 and computador == 2:
    print('VOCÊ PERDEU!, o computador escolheu tesoura, e você escolheu papel.')
elif jogador == 3 and computador == 0:
    print('VOCÊ PERDEU!, o computador escolheu pedra e você escolheu tesoura.')
elif jogador == 3 and computador == 1:
    print('PARABÉNS VOCÊ VENCEU!, o computador escolheu papel e você escolheu tesoura.')
elif jogador == 3 and computador == 3:
    print('EMPATE!, você e a maquina escolheram tesoura.')

#jeito do professor
from random import randint
from time import sleep
intens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('O computador escolheu {}'.format(intens[computador]))#colocar intens no format na variavel computador, faz o computador usar os intens no lugar de numeros.
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 10)
print('O computador jogou {}'.format(intens[computador]))
print('O jogador jogou {}'.format(intens[jogador]))
print('-=' * 10)
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('O JOGADOR VENCEU!')
    elif jogador == 2:
        print('O COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print('O COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('OJOGADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 0:
        print('O JOGADOR VENCEU!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')