#Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadrastada, o programa deverá perguntar se o usuário
#quer ou não continuar. No final mostre:
#A) Quantas pessoas tem amis de 18 anos
#B) Quantos homens foram cadastrados
#C)Quantas mulheres tem mais de 20 anos
tot18 = toth = totm = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}.')
print(f'Total de homens: {toth}.')
print(f'Total de mulheres: {totm}')