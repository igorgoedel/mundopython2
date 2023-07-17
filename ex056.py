#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#Média de idade do grupo.
#Qual é o nome do mais velho.
#Quantas mulheres tem menos de 21 anos.
vinteum = 0
mediaidade = 0
maior = 0
nomez = ''
for c in range(1, 5):
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    mediaidade = mediaidade + idade#Ou mediaidae += idade
    idademedia = mediaidade / 4
    if c == 1 and sexo in 'Mm':
        maior = idade
        nomez = nome
    if sexo in 'Mm' and idade > maior:
        maior = idade
        nomez = nome
    if idade <= 21:
        vinteum += 1
print('A média de idade da lista é {}.'.format(idademedia))
print('O nome do mais velho é {} e a sua idade é {}.'.format(nomez, maior))
print('E {} mulheres tem menos de 21 anos de idade.'.format(vinteum))

#Jeito do professor
somaidade = 0#Para calcular a média idade do codigo eu preciso samor todas as idades do gurpo e depois dividilas por 4.
mediaidade = 0#Essa variavel vai ser usada para dividir as idades e descobrir a media idade.
maioridadehomem = 0#Essa variavel é usada para achar a idade do homem mais velho comparadnoe deic=xando dentro da variavel a idade mais alta.
totmulher20: int = 0
nomevelho = ''
for p in range (1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':#Se o sexo for masculino com M maiusculo e m minusculo, depende qual for a opçao do que estiver escrevendo.Se for masculino e for a maior idade do homem será a 'idade'.
        maioridadehomem = idade#Aqui será guardado dentro da variavel o valor.
        nomevelho = nome#Tudo dentro desse if só será feito se for o primerio nome da variavel maioridade.
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem,nomevelho))
print('Ao todo são  {} mulheres com menos de vinte anos.'.format(totmulher20))
#Nesse exercico são usadas variaveis fazias preenchidas por condicões, for é usado para idecsar as 4 pessoas do exercicio.