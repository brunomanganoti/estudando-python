import matplotlib.pyplot as plt

cidade_a = [32,30,27,28,29,24]
datas = [5,10,15,20,25,30]

# plt.bar(datas, cidade_a, width=1.25, color='r', label='Cidade A')
plt.barh(datas, cidade_a, height=1.25, color='r', label='Cidade A')
plt.legend()



plt.show()