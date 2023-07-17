#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio.
#Indo de 10 até 0, com uma pausa de 1 seg até eles.
from time import sleep
for c in range(10, 0, -1):
    print(c)
    sleep(0.5)
print('Kaaaatsu!')
sleep(0.5)
print('Buuuum! Kaabuuummm!')
sleep(10)
print('BUUUM!')

#Jeito do professor
from time import sleep
print('contagem regrecisava para os fogos..')
for c in range (10, -1, -1):
    print(c)
    sleep(0.5)
print("BUUM!")