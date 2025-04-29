# Funções lambda (anônimas)
# Sintaxe:
# lambda argumentos: expressão

""" quadrado = lambda x: x**2

for i in range(1,6):
    print(quadrado(i)) """

""" ehPar = lambda x: (x%2 == 0)
print(ehPar(9)) """

""" f_c = lambda f: (f - 32) * 5/9
print(f_c(32)) """

# Função map()
# Sintaxe:
# map(função, iterável)

""" num = [1,2,3,4,5]
dobro = list(map(lambda x: x*2, num))
print(dobro) """

palavras = ['Python', 'Linguagem', 'Programação']
up = " ".join(list(map(str.upper, palavras)))
print(up)