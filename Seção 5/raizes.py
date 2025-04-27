# Equação 2° grau: ax^2 + bx + c
# Delta = b^2 - 4ac

import sys
import os

def raizes(a, b, c):
    delta = ((b ** 2) - (4 * a * c))

    x1 = (-b + (delta ** (1/2))) / (2 * a)
    x2 = (-b - (delta ** (1/2))) / (2 * a)

    print(f'\nO valor de x1 é: {x1:.2f}')
    print(f'O valor de x2 é: {x2:.2f}\n')

    valores = []
    valores.append(x1)
    valores.append(x2)
    return valores

if __name__ == '__main__':
    while True:
        print(f'Calcular as raízes de uma equação de segundo grau.\n')
        print(f'Equação no formato: ax^2 + bx + c\n')

        try:
            a = float(input('Insira o valor de a: '))
            b = float(input('Insira o valor de b: '))
            c = float(input('Insira o valor de c: '))
        except ValueError:
            print('Digite somente números.')
        else:
            resultado = raizes(a, b, c)
            print(resultado)
        
        while True:
            continua = input('\nDigite q para sair ou n para novo cálculo: ')
            if (continua.lower() == 'q'):
                sys.exit()
            elif (continua.lower() == 'n'):
                os.system('cls')
                break
            else:
                print('Entrada inválida.')