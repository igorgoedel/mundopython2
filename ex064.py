#Crie um programa que leia varios números inteiros pelo teclado. o programa só vai parar quando o usuario digitar o valor
#999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconciderando o flog).
num = 0
cont = 0#O contador aqui recebe 0 porque ele não contou nada ainda.
soma = 0
num = int(input('Digite um número [999 para parar]: '))#Aqui foi feito uma manobra.
while num != 999:
    soma += num
    cont += 1#Depois que ele conta ele vai recebre mais um.
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números.'.format(cont))
print('A soma entre eles foi {}.'.format(soma))