#Melhore o desafio 061, perguntando para o usuario se ele quer mostrar mais alguns termos. o programa encerra quando
#Ele disser que quer mostrar 0 termos.
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:#Aqui teve que ser mudado porque o cliente pode querer algo amais que 10.
        print('{}'.format(termo),end=' → ')
        cont += 1
        termo += razão
    print('PAUSA!')
    mais = int(input('Quantos termos você quer mostrar mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
