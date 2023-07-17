#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
#De acordo com a tabela abaixo.
#Abaixo de 18.5: Abaixo do peso.
#Entre 18.5 e 25: Peso ideal.
#25 até 30: Sobrepeso.
#30 até 40: Obesidade.
#Acima de 40: Obecidade Móbida.
peso = float(input('Qual o seu peso? '))
altu = float(input('Qual a sua altura? '))
imc = peso / (altu ** 2)
if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc < 25:
    print('Parabéns, você está no peso ideal!')
elif imc < 30:
    print('você está com sobrepeso!')
elif imc < 40:
    print('Você está com obesidade!')
elif imc > 40:
    print('Você tem obesidade morbida!')

#Jeito do professor
peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Peso ideal.')
elif 25 <= imc < 30:
    print('Sobrepeso.')
elif 30 <= imc < 40:
    print('Obesidade.')
elif imc >= 40:
    print('Obecidade Morbida.')