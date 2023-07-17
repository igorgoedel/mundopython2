#Faça um programa que leia o ano de nascimento de um joven e informa de acordo com a sua idade.
#Se ele ainda vai se alistar no serviço militar.
#Se é a hora dele se alistar.
#Se ja passou do tempo do alistamento.
#Seu programa tambem deverá mostrar o tempo que falta ou passou do prazo.
from datetime import date
atual = date.today().year
data = int(input('Qual é seu ano de nascimento? '))
sex = str(input('Qual é o seu sexo: [M/F] ')).strip().upper()[0]
idade = atual - data
if sex == 'M':
    if idade == 19:
        print('Você nasceu no ano {} esse ano você deve se alistar!'.format(data))
    elif idade < 19:
        print('Você nasceu no ano de {}, portanto você já tem {} anos, faltam {} anos para você se alistar no serviço militar.'.format(data, idade, (idade - 19)))
    elif idade > 19:
        print('Você nasceu no ano de {}, portanto você tem {}, passaram {} anos para o alistamento militar.'.format(data, idade, (idade - 19)))
    else:
        print('Você digitou algo errado, Tente novamente!')
elif sex == 'F':
    print('Você não pode se alistar!')

# Jeito do professor
from datetime import date
atual = date.today().year
nasc = int(input('Qual é o ano do seu nascimento? '))
idade = atual - nasc
print('Quem nasceu no ano {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.')
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado no ano de {}.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamnto foi em {}.')