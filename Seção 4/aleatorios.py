import random

""" print('Cinco números aleatórios entre 1 e 50:\n')

 for i in range(5):
    n = random.randint(1,50)
    if n % 2 == 0:
        print(f'Número gerado: {n}') # apenas imprime se for par
    else:
        continue """

""" valor = random.random()
print(f'Número gerado: {round((valor * 10), 2)}') """

""" valor = random.uniform(10, 130)
print(f'Número gerado: {round(valor, 2)}') """

lista = [1,3,6,72,25,757,202,191]
""" num = random.choice(lista)
print(f'Número escolhido: {num}') """

""" num = random.sample(lista, 2)
print(f'Números escolhidos: {num}') """

# Demonstração - Embaralhar lista de números

print(f'Lista original:\n {lista}')
print(f'Lista embaralhada:')
emb = random.shuffle(lista)
print(lista)