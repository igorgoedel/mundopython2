#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
num = int(input('Escolha um número para a tabuada: '))
for c in range(0, 11):
    print('{} x {} = {}'.format(c, num, c * num))
print('Fim!')

#Jeito do professor
num = int(input('Escolha um número:'))
print('=-' * 12)
for c in range (0, 13):
    print('{} x {} = {}'.format(num, c, c * num))
print('-=' * 12)