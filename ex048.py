#Faça um programa que calcule a soma entre todos os números impares que são multiplos de três e que se encontram.
#No intervalo de 1 até 500.
#Esse exercício eu não concegui fazer, não concegui entender o enunciado.
#Esse é o jeito do professor
soma = 0#Esse é um acomulador, verá mais sobre ele nos exercicios da proxima aula.
cont = 0#Esse é um contador, ele é usado para contar sempre mais um, e o acomulador ele soma ou multiplica aquillo que precisamos.
for c in range(1, 501, 2):#Pulando de dois em dois só vou ter números impares na lista
    if c % 3 == 0:
        soma = soma + c#Esse jeito de escrever essa linha de codigo é o mesmo de escrever o de baixo.É como se desse certo se escrevesse os dois da mesma forma.
        cont += 1#Basicamente oque diz aqui e na variavel a cima é que cont ou soma, recebe soma ou cont mais o número, no caso de cont é cont +1, no caso de soma recebe mais c.
print('A soma de todos os {} valores solicitados é {}.'.format(cont, soma))