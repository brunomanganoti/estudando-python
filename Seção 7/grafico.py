from matplotlib import pyplot as plt

plt.style.use('bmh')

eixo_x_dias =    [1,5,10,15,20,25,30]
eixo_y_tempmax = [28,29,25,32,34,36,31]
eixo_y_tempmin = [21,22,17,23,16,24,20]

plt.title('Temperaturas máximas e mínimas')
plt.xlabel('Dias')
plt.ylabel('Temperaturas')

plt.plot(eixo_x_dias, eixo_y_tempmax, linestyle='--', marker='o')
plt.plot(eixo_x_dias, eixo_y_tempmin, color='#1ddfa5', linewidth=1)

# primeiro plot = primeira legenda
plt.legend(['Temp Máx.', 'Temp Mín.'])

# plt.grid(True)
# print(plt.style.available)
plt.show()