from matplotlib import pyplot as plt

plt.style.use('bmh')

eixo_x_dias =    [1,5,10,15,20,25,30]
eixo_y_tempmax = [28,29,25,32,34,36,31]
eixo_y_tempmin = [21,22,17,23,16,24,20]

plt.title('Temperaturas máximas e mínimas')
plt.xlabel('Dias')
plt.ylabel('Temperaturas')

plt.bar(eixo_x_dias, eixo_y_tempmax, label='Temp Máx')
plt.plot(eixo_x_dias, eixo_y_tempmin,color='#550099',label='Temp Mín')

# primeiro plot = primeira legenda
plt.legend(loc='best')

# plt.grid(True)
# print(plt.style.available)

""" plt.axis([1,31,5,45])
print(plt.axis()) """
""" plt.ylim([-5,50])
plt.xlim([1,31]) """
# plt.savefig('grafico.png')

# Plotar gráfico de uma função como f(x) = x^3 + 1
""" x = range(1,11,1)
plt.plot(x, [(num**3 + 1) for num in x]) """

plt.show()