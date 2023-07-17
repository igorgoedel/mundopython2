#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F. Caso esteja errado.
#Peça a digitação novamante até que esteja correto.
sexo = str(input('informe seu sexo: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados informados errados, por favor digite novamente: ')).strip().upper()[0]
if sexo == 'M':
    print('Sexo masculino armazenado com sucesso!')
elif sexo == 'F':
    print('Sexo feminino armazenado com sucesso!')

#Jeito do prefessor
sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]#aqui ele tira os espaços e com o upper ele pega apenas a pimeira letra.Esse [0] é um fatiamento visto nas primeiras aulas.
while sexo not in 'MmFf':#Enquanto o sexo não estiver em MmFf
    sexo = str(input('Dados inválidos, Por favor informe seu sexo:')).strip().upper()[0]
print('Sexo {} Registrado com sucesso'.format(sexo))