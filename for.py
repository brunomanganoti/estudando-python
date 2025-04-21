#nome = input('Insira seu nome: ')

""" for x in range(10):
    print(f'{x+1}: {nome}')
print('Laço \'For\' encerrado.') """

# range(valorInicial, valorFinal, incremento)
""" for x in range(2,20,2):
    print(x) """

pedras = ['Rubi', 'Quartzo', 'Topázio', 'Lazurita']

for pedra in pedras:
    if (pedra == 'Quartzo'):
        continue
    print(pedra)