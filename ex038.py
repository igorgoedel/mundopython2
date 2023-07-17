#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#O primerio valor é maior.
#O segundo valor é maior.
#Não existe valor maior, os dois valores são iguais.
num = int(input('Escreva um número inteiro:' ))
num1 = int(input('Escreva outro número inteiro: '))
if num > num1:
    print('O primeiro número digitado {}, é maior que o segundo número {}!'.format(num, num1))
elif num1 > num:
    print('O Segundo número digitado {}, é maior que o segundo número digitado {}!'.format(num1, num))
else:
    print('Os dois números digitados são iguais!')

#Jeito do professor
n1 = int(input('Pimeiro número: '))
n2 = int(input('Segundo número'))
if n1 > n2:
    print('O primeiro número é o maior!')
elif n2 > n1:
    print('O Segunro número digitado é o maior!')
else:
    print('Os dois números são iguais!')