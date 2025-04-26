# Funções
# Modularização, Reuso de código, Legibilidade
# Funções internas (built-in) e definidas pelo usuário

""" def <nome_funcao> ([argumentos]):
    <instruções> """

def mensagem():
    print(f'Mensagem da função!')
    print(f'Curso de Python')
# mensagem()

# Função com argumentos
""" def soma(num1, num2):
    print(num1 + num2)

soma(4, 25) """

def mult(x, y):
    return x * y

""" a = 5
b = 20

multiplicacao = mult(a, b)
print(f'O produto de {a} e {b} é: {multiplicacao}') """

def div(k, j):
    if j != 0:
        return (k / j)
    else:
        return 'Não é permitida divisão por 0.'

""" if __name__ == '__main__':
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))

    r = div(a, b)
    print(f'{a} divido por {b} é igual a {r}') """

def quadrado(valor):
    quadrados = []
    for x in valor:
        quadrados.append(x ** 2)
    return quadrados

def juntaNome(nome, sobrenome):
    return nome + ' ' + sobrenome

def contar(num=11, caractere='+'):
    for i in range(1, num):
        print(caractere, end=' ')

def soma_mult(a, b, c = 0):
    if c == 0:
        return a * b
    else:
        return a + b + c

if __name__ == '__main__':
    """ valores = [2, 5, 9, 12, 21]
    resultados = quadrado(valores)
    for q in resultados:
        print(q)
    
    nome = str(input('Insira o primeiro nome: '))
    sobrenome = str(input('Insira o sobrenome: '))
    nome_completo = juntaNome(nome, sobrenome)

    print(nome_completo) 

    contar(6, '@') """

    res = soma_mult(5, 6)     # Apenas multiplicação
    res = soma_mult(5, 6, 10) # Soma
    print(res)