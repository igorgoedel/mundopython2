#Condições aninhadas
nome = str(input('Qual é o seu nome ?'))
if nome == 'Igor':
    print('Que nome bonito você tem!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem norma.')
print('Tenha um bom dia, {}!'.format(nome))
