#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores
#e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele não continuar a digitar valores.
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar?[N/S] ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} e a media foi {}.'.format(num, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))