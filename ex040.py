#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
#de acordo com a média atingida:
#Média abaixo de 5.0 = REPROVADO.
#Média entre 5.0 e 6.9 = RECUPERAÇÃO.
#Média 7.0 ou superior = APROVADO.
#nota0 = float(input('Primeira nota: '))
#nota1 = float(input('Segunda nota: '))
#notafinal = (nota0 + nota1) / 2
#if notafinal < 5.0:
#    print('Sua nota foi {}, Você está reprovado!'.format(notafinal))
#elif notafinal > 5.0 and < 7:
#    print('Sua nota foi {}, Você está em RECUPERAÇÃO!')
#elif notafinal > 7.0:
#    print('Sua nota foi {}, Você está APROVADO!')

#Jeito do professor
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a medida do aluno é {:.1f}'.format(nota1, nota2, média))
if 7 > média >= 5:
    print('O aluno está em RECUPERAÇÃO!')
elif média < 5:
    print('O aluno est[a REPROVADO!')
else:
    print('O aluno está aprovado.')