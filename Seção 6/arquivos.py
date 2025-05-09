# Manipulação de arquivos de texto

# manipulador = open('arquivo.txt', 'r', encoding='utf-8')
""" print(f'\nMétodo read():\n')
print(manipulador.read()) """

""" print(f'\nMétodo readline():\n')
print(manipulador.readline()) """

""" print(f'\nMétodo readlines():\n')
print(manipulador.readlines()) """

""" texto = str(input('Qual termo deseja procurar no arquivo? '))
print('')

try:
    # manipulador = open('C:\\Users\\Pichau\\Documents\\OFL.txt', 'r', encoding='utf-8')
    # manipulador = open('arquivo1.txt', 'r', encoding='utf-8') -> IOError
    manipulador = open('arquivo.txt', 'r', encoding='utf-8')
    
    num_linha = 0
    for linha in manipulador:
        num_linha += 1
        if texto in linha:
            linha = linha.rstrip()
            print(f"Termo encontrado na linha '{num_linha}':")
            print('"' + linha + '"\n')
        else:
            print(f"Termo não encontrado na linha '{num_linha}'.\n")
except IOError:
    print('Não foi possível abrir o arquivo.')
else:
    manipulador.close() """

# Escrever em arquivos de texto
""" texto = '\nTexto texto texto texto texto'
try:
    manipulador = open('arquivo.txt', 'a', encoding='utf-8')
    # manipulador.write('Teste de write no arquivo\n')
    # manipulador.write('Manipulando um arquivo de texto com python')
    # manipulador.write('\nAdicionando texto ao arquivo utilizando append (a)')
    manipulador.write(texto)
except IOError:
    print('Não foi possível abrir o arquivo.')
else:
    manipulador.close() """

# Método writelines():
frutas = ['Morango\n', 'Framboesa\n', 'Caju\n', 'Amora']
try:
    manipulador = open('frutas.dat', 'w', encoding='utf-8')
    manipulador.writelines(frutas)
except IOError:
    print('Não foi possível abrir o arquivo.')
else:
    manipulador.close()

# Ler o arquivo criado (frutas.dat)
try:
    manipulador = open('frutas.dat', 'w', encoding='utf-8')
    manipulador.writelines(frutas)
except IOError:
    print('Não foi possível abrir o arquivo.')
else:
    manipulador.close()