# Trocar valores entre duas variáveis
# -----------------------------------
var1 = 12
var2 = 31

""" var1, var2 = var2, var1
print(var1)
print(var2) """

# Operador condicional ternário
# -----------------------------
""" menor = var1 if var1 < var2 else var2
print(f'Menor valor: {menor}')
print(f'Menor valor: {(var2, var1)[var1 < var2]}') """

# Generators
# ----------
""" valores = [1,3,6,7,9,11,13,15]
quadrados = (item ** 2 for item in valores)
# print(quadrados)
for quadrado in quadrados:
    print(quadrado, end=' ') """

# Função enumerate()
# ------------------
""" bebidas = ['Café', 'Chá', 'Água', 'Suco', 'Refrigerante']
for i, item in enumerate(bebidas):
    print(f'Índice: {i}, Item: {item}') """

""" temperaturas = [-1, 10, 5, -3, 8, 4, -2, -5, 7]
total = 0

neg_temp = []
for i, temp in enumerate(temperaturas):
    if temp < 0:
        total += 1
        neg_temp.append(i)
# print(f'Há {total} temperaturas negativas')
print(f'Há {total} temperaturas negativas nos índices: {neg_temp}') """

# Gerenciamento de contexto com with
# ----------------------------------
try:
    a = open('frutas.dat', 'r', encoding='utf-8')
    print(a.read())
except IOError:
    print('Não foi possível abrir o arquivo.')
else:
    a.close()

with open('frutas.dat', 'r', encoding='utf-8') as a:
    for linha in a:
        print(linha, end="")