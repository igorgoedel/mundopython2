#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo.
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()#Aqui ele vai dividir a frase em palavras
junto = ''.join(palavras)#Aqui ele vai juntas todas as palavras descociderando os espaços, ou seja ele eliminou os espaços de antes e depois com o slipt e eliminou os espaços internos com join.
print('Você digitou a frase {}'.format(frase))
inverso = ''#Aqui ele precisa varrer a string de trás pra frente pra que conciga a string inversa.
for letra in range(len(junto) -1, -1, -1):#Aqui ele vai pegar o número de letras do junto, vai tirar um, vai até a letra menos um que é antes da primeira, e vai voltando uma letra.
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:#Se inverso é igual a junto é sinal de que ele é um palíndromo.
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
