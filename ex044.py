#Elabroe um programa que calcule o valor a ser pago por um produto conciderado o seu preço normal e condição de pagamento:
#Á vista dinheiro/cheque 10% de desconto.
#Á vista no cartão 5% de desconto.
#Em até 2x no cartão: preso normal.
#3x ou mais no cartão: 20% de juros.

preco = float(input('Qual é o preço? '))
print('''O pagamento vai ser:
[ 1 ] A vista dinheiro ou cheque
[ 2 ] A vista no cartão
[ 3 ] Em até 2x no cartão
[ 4 ] Em até 3x no cartão''')
escolha = int(input('Digite sua escolha: '))
if escolha == 1:
    print('O preço do produto é {} reais, com o desconto de 10% ele ficará {:.2f} reais.'.format(preco, preco -(preco * 10 / 100)))
elif escolha == 2:
    print('O preço do produto é {} reais, com o desconto de 5% ele ficará {:.2f} reais.'.format(preco, preco - (preco * 5 / 100)))
elif escolha == 3:
    print('O preço do produto é {} reais, ele ficará em 2x de {:.2f} reais.'.format(preco, preco / 2))
elif escolha == 4:
    print('O preço do produto é {} reais, ele ficará em 3x de {:.2f} reais.'.format(preco, (preco + ( preco * 20 / 100)) / 3))

#Jeito do professor
print(' ========== LOJAS GUANABARA ========== ')
preco = float(input('Preço das compras: R$ '))
print('''FOMRAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão 
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}.'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalpre = (int(input('Quantas parcelas? ')))
    parcela = total / totalpre
    print('Sua compra será parcela em {}x de {:.2f} COM JUROS!'.format(totalpre, parcela))
else:
    total = 0
    print('Opção invalida de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))