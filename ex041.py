#A confederação Nacional de Natação precisa de um programa que leia o ano  de nascimento de um atleta e mostre.
#Sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JUNIOR
#Até 20 anos: SÊNIOR
#Acima: MASTER
from datetime import date
atual = date.today().year
nasc = int(input('Qual o seu ano de nascimento ?'))
idade = atual - nasc
if idade <= 9:
    print('Você tem {} anos, Sua categoria é MIRIM!'.format(idade))
elif 9 > idade <= 14:
    print('Você tem {} anos, Sua categoria é INFANTIL!'.format(idade))
elif 14 > idade <= 19:
    print('Você tem {} anos, Sua caegoria é JUNIOR!'.format(idade))
elif 19 > idade <= 20:
    print('Você tem {} anos, Sua categoria é SÊNIOR!'.format(idade))
elif idade > 20:
    print('Você tem {} anos, Sua categoria é MASTER!'.format(idade))

#Jeito do professor
from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')