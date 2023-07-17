num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezeseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    numero = int(input('Digite um número de zero a vinte: '))
    if 0 <= numero <= 20:
        break
    print('Tente novamente..')
print('O número que você digitou foi {}'.format(num[numero]))
resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
while resp not in 'SN':
    if resp == 'N':
        print('Fim do programa..')
    elif resp == 'S':
        numero = int(input('Digite um número de zera a vinte: '))
    elif 0 <= numero <= 20:
        print('Tente novamente..')
    else:
        break
print('O número que você digitou foi {}'.format(num[numero]))