#Crie um programa que leia o nome e preço de varios produtos. O programa deverá perguntar se o usuário vai continuar.
#No final mostre :
#Qual é o preço gasto na compra
#Quantos produtos custam mais de 1000.
#Qual é o nome do produto mais barato.
total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço do produto: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos acima de mil rais.')
print(f'O produto mais barato foi {barato} que custa custa R${menor:.2f}')