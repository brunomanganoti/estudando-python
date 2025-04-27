# Recursividade

def fatorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * fatorial(n-1)
    
""" print(fatorial(0))
print(fatorial(1))
print(fatorial(4))
print(fatorial(5))
print(fatorial(6))
print(fatorial(7)) """

if __name__ == '__main__':
    try:
        n = int(input('Insira um número inteiro: '))
        if ((n < 0) or (not (isinstance(n, int)))):
            raise ValueError
    except ValueError:
        print('Insira um número positivo e inteiro.')
    else:
        try:
            fat = fatorial(n)
        except RecursionError:
            print('O número fornecido é muito grande.')
        else:
            print(f'O fatorial de {n} é: {fat}')

