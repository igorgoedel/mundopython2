#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite uma valor: '))
if num % num:
    print('O número que você digitou não é número primo')
else:
    print('O número que você digitou não é um número primo')

#Jeito do professor
num = int(input('Digite um número: '))
tot = 0#Variável criada para saber o número de divisíveis.
for c in range(1, num + 1):#Mais um sempre porque o python conta sempre menos um dentro do for.
    if num % c == 0:#Se o número for divisivel pelo contador, porque ele vai contar de 1 até o num.Assim todos os números divisiveis ficarão coloridos.
        print('\033[34m', end='')
        tot += 1#Se o número for divisivel é mais um no total, por isso ele esté idecsado no if.
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')#Esse rpint está indecsado ao if abaixo do for.
print('\n\033[mO número {} foi divisível {} vezes.'.format(num, tot))#Esse trexo do codigo está indecsado fora if.
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele não é PRIMO!')
