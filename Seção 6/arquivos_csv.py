import csv

""" with open('elementos.csv', mode='r', encoding='utf-8') as arq:
    leitor = csv.reader(arq, delimiter=',')
    cont_linhas = 0

    for linha in leitor:
        if cont_linhas == 0:
            print(f'Colunas: {" ".join(linha)}\n')
            cont_linhas += 1
        else:
            print(f'Elemento: {linha[1]}, Símbolo: {linha[2]}, Grupo: {linha[3]}')
            cont_linhas += 1
    
    print(f'\nForam lidas {cont_linhas} linhas...') """

simbolos = []
with open('elementos.csv', mode='r', encoding='utf-8') as arq:
    leitor = csv.reader(arq)
    for idx, linha in enumerate(leitor):
        if idx == 0:
            pass
        else:
            simbolos.append(linha[2])
    print(simbolos)

# Adicionando mais conteúdo ao arquivo 'elementos.csv'
""" with open('elementos.csv', mode='a', encoding='utf-8', newline='') as arq:
    escritor = csv.writer(arq, delimiter=',')
    escritor.writerow(['7','Nitrogenio','N','15'])
    escritor.writerow(['8','Oxigenio','O','16'])
    escritor.writerow(['9','Fluor','F','17']) """