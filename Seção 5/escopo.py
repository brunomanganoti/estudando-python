# Escopo global e local

var_global = "Curso completo de Python"

def escreve_texto():
    global var_global
    var_global = "Banco de Dados"
    var_local = "Bruno"
    print(f'Variábel global: {var_global}')
    print(f'Variábel local: {var_local}')

if __name__ == '__main__':
    print(f'Executar a função escreve_texto()')
    escreve_texto()

    print('\nTentar acessar as variáveis diretamente:')
    print(f'Variábel global: {var_global}')
    # print(f'Variábel local: {var_local}') - não acessível
    print('\n')