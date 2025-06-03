import matplotlib.pyplot as plt

# Temperaturas
""" cidade_a = [32,30,27,28,29,24]
cidade_b = [27,26,29,25,22,22]
cidade_c = [17,19,15,20,25,26] """

# Homicídios
cidade_a = [5,2,0,0,2,1]
cidade_b = [2,1,2,4,3,6]
cidade_c = [8,5,2,0,2,6]

datas = [5,10,15,20,25,30]

# Posições distintas para cada cidade
""" posicoes_a = list(range(len(datas)))
posicoes_b = [pos + .25 for pos in posicoes_a]
posicoes_c = [pos + .5 for pos in posicoes_a] """

# plt.barh(datas, cidade_a, height=1.25, color='r', label='Cidade A')

plt.bar(datas, cidade_a, color='r', label='Cidade A')
plt.bar(datas, cidade_b, bottom=cidade_a, color='g', label='Cidade B')
plt.bar(datas, cidade_c, bottom=[a+b for a, b in zip(cidade_a, cidade_b)], color='b', label='Cidade C')

plt.legend()
# plt.xticks(ticks=posicoes_a, labels=datas)
plt.xlabel('Datas')
plt.ylabel('Homicídios')
plt.title('Homicídios nas Cidades em Dias Determinados')

plt.show()