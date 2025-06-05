import matplotlib.pyplot as plt

linguagens = ['Python', 'JavaScript', 'C#', 'Ruby']
quantidades = [300,270,150,40]
cores = ('#660033', 'blue', 'yellow', 'g')
distancia = (0, 0, 0.1, 0.1)

plt.pie(quantidades, labels=linguagens, autopct='%1.1f%%', startangle=90, shadow=True, colors=cores, explode=distancia)

plt.title('Preferências por linguagens de programação')
plt.legend(title='Linguagens', loc='best', bbox_to_anchor=(1, .8))

plt.show()