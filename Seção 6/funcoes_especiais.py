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

""" palavras = ['Python', 'Linguagem', 'Programação']
up = " ".join(list(map(str.upper, palavras)))
print(up) """

# Função filter
# Sintaxe:
# filter(função, sequência)

def ehPar(num):
    return num % 2 == 0

nums = [1,2,3,4,5,6,7,8,9,10,24]

""" nums_par = list(filter(ehPar, nums))
print(nums_par) """

""" nums_impar = list(filter(lambda n: n % 2 != 0, nums))
print(nums_impar) """

# Função reduce()
# Sintaxe:
# reduce(função, sequência, valor_inicial)

from functools import reduce

""" def mult(x, y):
    return x * y

numeros = [1,2,2,3,4,6]

nums_mult = reduce(mult, numeros)
print(nums_mult) """

# Soma cumulativa dos quadrados de valores usando expressão lambda

numeros = [1,2,3,4]

def soma(x, y):
    return x + y

soma_quadrados = reduce(lambda x, y: x**2 + y**2, numeros)
print(soma_quadrados)