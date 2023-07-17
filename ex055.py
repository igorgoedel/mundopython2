#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor dos pesos lidos.
menor = 0
maior = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if c == 1:#É preciso ler o primeiro laço para dar a continuidade ao código, se não ler nenhum laço o código não roda.
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O menor peso digitado foi {:.2f}, e o maior foi {:.2f}.'.format(menor, maior))

#Jeito do professor
maior = 0
menor = 0
for c in range (1,6):#For in c é c porque é c de contador.
    peso = float(input('Digite o peso da {}ª pessoa:'.format(c)))
    if c == 1:#Quer dizer que eu acabei de ler o primeiro peso.
        maior = peso#O maior peso vai passar a ser o peso.
        menor = peso#O menor peso vai pasar a ser o peso.
    else:#Se não
        if peso > maior:#O peso que eu acabei de ler for maior que o maior peso que eu tenho.
            maior = peso#O maior peso passa a ser o maior peso que eu acabei de ler.
        if peso < menor:#Se o peso for menor que o menor peso.
            menor = peso#O menor peso passa a ser o peso.
print('O maior peso lido foi de {}kg.'.format(maior))
print('O menor peso lido foi de {}kg.'.format(menor))