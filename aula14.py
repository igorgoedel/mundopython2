'''for c in range (1, 10):
    print(c)
print('Fim')'''

c = 1#O contador começa com 1. que é o inicio do range.
while c < 10:#Enquanto o contador for menor que 10.
    print(c)
    c = c + 1#Ou então c += 1, porque eu quero que quando ele volte eu some mais um no c.
print('Fim')
#Quando vocÊ quer repetir a mesma string com for.
'''for c in range(1, 5):
    valor = int(input('Digite um valor: '))
print('Fim!')'''

#ESse é um exemplo que difenrencia o for do while, em while só vai parar de repetir a sting quando for digitado 0, em for ele ja tem um número estabelecido de repetições.
valor = 1
while valor != 0:
    valor = int(input('Digite um valor: '))
print('Fim!')

#Isso não da pra fazer com o for, no while você não determina um range. R é um flag, uma condição de parada.
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')

#Aqui é uma verificação de números pares e impares digitados, mas no final do codigo a resposta conta a flag que no casa aqui é 0.
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print('Você digitou {} números pares e {} números impares!'.format(par, impar))

#Aqui é uma gambiarra feita para resolver o problema do codigo acima, gambiarra feita porque o curso só usa recursos encinados em aula.
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números impares!'.format(par, impar))
#Compare esse código com o código acima.