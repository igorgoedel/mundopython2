#Crie um programa que leia dois valores e mostre um menu e como o ao lado na tela:
#Seu programa deverá realizar a operação solicitada em cada caso
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos números
#[5] sair do programa
num1 = float(input('Digite um valor: '))
num2 = float(input('Digite outro valor: '))
escolha = 0
while escolha != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do Programa''')
    escolha = int(input('Faça a sua escolha: '))
    if escolha == 1:
        print('A soma entre {:.2f} e {:.2f} é {:.2f}.'.format(num1, num2, num1 + num2))
    elif escolha == 2:
        print('A multiplicação entre {:.2f} e {:.2f} é {:.2f}'.format(num1, num2, num1 * num2))
    elif escolha == 3:
        if num1 > num2:
            print('O maior entre {:.2f} e {:.2f} é {:.2f}'.format(num1, num2, num1))
        else:
            print('O maior entre {:.2f} e {:.2f} é {:.2f}.'.format(num1, num2, num2))
    elif escolha == 4:
        num1 = float(input('Digite um novo número: '))
        num2 = float(input('Digite outro novo número: '))
    elif escolha == 5:
        print('Programa finalizado com sucesso.')
    else:
        print('Escolha invalida tente novamente!')

#Jeito do professor
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    '''[ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa'''
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma de {} e {} é {}.'.format(n1, n2, soma))
    elif opcao == 2:
        multiplicacao = n1 * n2
        print('A multiplicação entre {} e {} é {}.'.format(multiplicacao))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}.'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente. ')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! volte sempre!')