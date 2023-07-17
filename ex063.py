#Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primerios elementos de uma sequencia de fibonancci.
#Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8
print('-=' * 30)
print('Sequência de Fibonacci')
print('-=' * 30)
n = int(input('Quantos termos você quer mostrar?'))
t1 = 0
t2 = 1
print('˜' * 30)
print('{} → {}'.format(t1,t2),end='')
cont = 3#O contador começa a contar no 3 porque no programa ja está indicado os dois primeiros números.
while cont <= n:
    t3 = t1+ t2
    print(' → {}'.format(t3),end='')
    t1 = t2#Aqui dentro da estrutura de repetição o t1 passa ser o t2 e o t2 passa a ser o t3, tudo para rodar o código.
    t2 = t3
    cont += 1
print(' → FIM')