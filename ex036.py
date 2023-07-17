#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa, o programa vai perguntar
#O valor da casa o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negado.
casa = float(input('Valor da casa: R$ '))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento ?'))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
if prestação <= mínimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')