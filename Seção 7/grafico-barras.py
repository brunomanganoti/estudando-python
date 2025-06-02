import matplotlib.pyplot as plt

cidade_a = [32,30,27,28,29,24]
cidade_b = [27,26,29,25,22,22]
cidade_c = [17,19,15,20,25,26]
datas = [5,10,15,20,25,30]

# Posições distintas para cada cidade
posicoes_a = list(range(len(datas)))
posicoes_b = [pos + .25 for pos in posicoes_a]
posicoes_c = [pos + .5 for pos in posicoes_a]

# plt.barh(datas, cidade_a, height=1.25, color='r', label='Cidade A')

plt.bar(posicoes_a, cidade_a, width=.25, color='r', label='Cidade A')
plt.bar(posicoes_b, cidade_b, width=.25, color='g', label='Cidade B')
plt.bar(posicoes_c, cidade_c, width=.25, color='b', label='Cidade C')
plt.legend()



plt.show()