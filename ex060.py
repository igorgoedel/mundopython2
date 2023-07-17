#Faça um programa que leia um número qualquer e mostre o seu fatorial EX:
#5!=5x4x3x2x1 = 120
#Sim tem um módulo para calcular fatoriais em python.
from math import factorial
n = int(input('Digite um valor para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))

n = int(input('Digite um número para calcular seu fatorial:'))
c = n#Esse é o contador que vai começar em n que é o número que eu acabei de ler.
f = 1
print('Calculando {}!'.format(n),end ='')
while c > 0:#Enquanto o contador for maior que zero.
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')#Aqui é escreva x se o c for maior do que 1 se não escreva um =.
    f *= c#Fatorial recebe o fatorial * o c
    c -= 1#Aqui diz que o c vai ser menos igual a um. Que c recebe c menos um.
print('{}'.format(f))#Aqui fica fora da indentação para que ele possa ser executado so depois do calculo final.

n = int(input('Digite um valor: '))
c = n
f = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))