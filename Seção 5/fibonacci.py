# Fibonacci recursivo

def fibonacci(num):
    if (num == 1):
        return [0]
    elif (num == 2):
        return [0, 1]
    else:
        fibo = fibonacci(num - 1)
        fibo.append(fibo[-1] + fibo[-2])
        return fibo

if __name__ == '__main__':
    try:
        num = int(input('Insira a quantidade para sequência: '))
        res = fibonacci(num)
        print(f'\nSequência de Fibonacci ({num}): {res}')
    except RecursionError:
        print('Número muito grande ou negativo.')
    else:
        print('\nFim do procedimento.')