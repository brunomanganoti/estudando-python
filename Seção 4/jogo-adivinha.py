import random
import os

opc = 's'
t = 1

while opc == 's':
    valor = random.randint(1, 15)
    print('-------------------------------------')
    print('-------- Jogo da Adivinhação --------\n')
    
    for i in range(3):
        print(f'Tentativa: {t}')
        tentativa = int(input('Insira o número (entre 1 e 15): '))
        
        if tentativa == valor:
            print('Parabéns, você acertou!')
            break
        elif tentativa > valor:
            print(f'Alvo é menor...\n')
            t += 1
        else:
            print(f'Alvo é maior...\n')
            t += 1
    
    opc = str(input(f'Você perdeu. O número era: {valor}\nInsira <S> para jogar novamente ou outra tecla para sair: '))
    opc = opc.lower()
    t = 1
    os.system('cls')