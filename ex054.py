#Crie um programa que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maior idade e quantas ja são maiores.
from datetime import date
atual = date.today().year
menor = 0
maior = 0
for c in range(0, 7):
    data = int(input('Digite a data de nascimento: '))
    idade = atual - data
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('São menores de idade e {} são maiores de idade {}.'.format(menor, maior))

#Jeito do professor
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    print('Essa pessoa tem {} anos'.format(idade))
    if idade >= 21:
        #print('Essa pessoa é maior')Tirei o print para mostrar oque a variavel tot esté subtituindo.
        totmaior += 1
    else:
        #print('Essa pessoa é menor')
        totmenor -= 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))