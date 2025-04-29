n1 = n2 = 0.0
media = 0.0
faltas = 0

n1 = float(input('Insira a primeira nota: '))

n2 = float(input('Insira a segunda nota: '))

faltas = int(input('Insira a quantidade de faltas: '))

media = (n1 + n2) / 2

if (faltas > 10):
    print('Aluno reprovado por faltas!')
elif (media >= 7):
    print('Aprovado. Média:', media)
    print('Parabéns!')
elif (media >= 5):
    print('Aluno de recuperação. Média:', media)
else:
    print('Reprovado. Média:', media)