#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar de digitar quando o usuário digitar
#O valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
#(Desconciderando o flag).
num = cont = soma = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    cont += 1
    soma += num
print('Você digitou {} e a media deles foi {}.'.format(cont, soma))