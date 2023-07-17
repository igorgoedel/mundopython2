for c in range(1, 6):#Ele escreve de 1 até 5 porque o contador não concidera o ultimo número. Mas se colocar o 0 no luagr do 1 ele aparecerá com o ultimo número.
    print('Oi!')
print('FIM!')
#Veja a diferença de indentação.
for c in range (0, 6):
    print('Oi!')
print('Fim!')
#Veja se colocar c.
for c in range (0, 6):
    print(c)
print('Fim!')
#Se você quiser que ele conte para trás.
#Oque acontece aqui é que ele começa no 6 e tira um e depois vai dessa forma, tirando de um em um.
#Oque acontece com o número -1 é a iteração, oque acontece no final do laço, que no caso vai tirar um.
for c in range (0, 6, -1):
    print(c)
#Se você quiser contar de 0 até 6 pulando de 2 em dois.
for c in range (0, 6, 2):
    print(c)
print('Fim!')

num = int(input('Digite um número: '))
for c in range (0, num+1):
    print(c)
print('FIM')
#No exercício abaixo ele usa os números digitados nas variáveis para formar o for.
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim')
#No exercício abaixo ele usa o for pra repetir a mesma variável 3 vezes.
for c in range(0, 3):
    n = int(input('Digirte um valor: '))
print('Fim!')
#No exercico abaixo, mostra como fazer um somatório dos números inputados.
s = 0
for c in range(0, 4):
    num = int(input('Digite um valor: '))
    s += num
print('Fim!, O somatório foi {}.'.format(s))