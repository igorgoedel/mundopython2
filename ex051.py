#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#No final, mostre os os 10 primeiros termos dessa progressão.
num = int(input('Primeiro termo: '))
num1 = int(input('razão: '))
for c in range(num, 10, num1):#Esse codigo não funciona porque aqui ele só vai contar até 10.
    print('{}'.format(c), end=' ')

#Jeito do professor
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão#Por isso para conceguir os 10 números foi preciso fazer essa variavel, o decimo termo precisou ser calculado.
for c in range (primeiro, décimo + razão, razão):#Então aqui fica o primeiro termo qua vai até o decimo termo pulando pela razão.
    print('{}'.format(c), end=' -> ')
print('ACABOU')
