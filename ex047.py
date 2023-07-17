#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
print('-=' * 30)
print('Todos os números pares de 0 a 50.')
print('=-' * 30)
for c in range(0, 51, 2):
    print(c, end=' ')

#Jeito do professor.
for c in range (1, 51):
    print('.', end=' ')#Esse ponto vai me dizer quantas vezes o processador fez o laço.
    if c % 2 == 0:
        print(c, end=' ')

#Esse é o código que fica mais leve para o processador.
for n in range (2, 51, 2):
    print(n, end=' ')
    print('Acabou!')