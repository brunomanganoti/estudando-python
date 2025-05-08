import os

os.chdir('C:\\teste')
print(f"Diretório atual: '{os.getcwd()}'")

nome_padrao = str(input('Insira o padrão de nomes de arquivo a ser utilizado (sem a extensão): '))

for contador, arq in enumerate(os.listdir()):
    if os.path.isfile(arq):
        nome_arq, exten = os.path.splitext(arq)
        # print(f'Nome: {nome_arq}\nExtensão: {exten}')
        nome_arq = nome_padrao + str(contador)

        nomearq_novo = f'{nome_arq}{exten}'
        os.rename(arq, nomearq_novo)

print('\nProcesso finalizado.')