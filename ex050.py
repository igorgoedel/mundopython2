#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#Se o valor digitado for impar desconcidere-o.
soma = 0
cont = 0
for num in range(1, 7):
    c = int(input('Digite o {} número: '.format(num)))
    if num % 2 == 0:
        soma += c
        cont += 1
print('Você informou {} números PARES e a soma foi {}.'.format(cont, soma))