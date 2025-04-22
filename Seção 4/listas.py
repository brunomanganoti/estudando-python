# Sintaxe: nome_lista = [valores]

notas = [2,5,10,20,50,100]
#print(notas)

notas2 = [4, 15, 19, 21]

# Concatena as listas
concat = notas + notas2

# Ordena a concatenação das listas
# concat.sort()

# print(concat[-1])

# Altera o último valor da lista
concat[-1] = 90

# Imprime os 4 primeiros valores
# print(concat[0:4])

# Imprime todos os valores
# print(concat[0:])

# Tamanho da lista
# print(len(concat))

# Lista ordenada sem alterar seus valores
# print(sorted(concat))

# Lista reversamente ordenada sem alterar seus valores
# print(sorted(concat, reverse=True))

""" print(sum(concat)) # soma dos valores
print(min(concat)) # menor valor 
print(max(concat)) # maior valor """

concat.append(188)
# print(concat)

concat.pop(0)
# print(concat)

concat.insert(0, 144)
# print(concat)

# print(144 in concat)  #true
# print(8099 in concat) #false

""" cidadespr = ['Maringá', 'Sarandi', 'Pitanga', 'Guarapuava', 'Londrina']
for cidade in cidadespr:
    if cidade[-1:].lower() == 'a':
        print(cidade) """

posicoes = ['primeiro', 'segundo', 'terceiro']
lista_nomes = []
for i in range(3):
    nome = str(input(f'Insira o {posicoes[i]} nome: '))
    lista_nomes.append(nome)

# print(f'Lista gerada: {lista_nomes}')

lista_nomes.sort()

print(f'Lista gerada:')
for nome in lista_nomes:
    print(f'    - {nome}')