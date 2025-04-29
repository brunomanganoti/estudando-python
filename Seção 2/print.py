# sintaxe: print(objetos, argumentos, ...)

""" print('Imprime a mensagem e pula linha')
print('Imprime a mensagem e continua na mesma linha.', end='')
print(' Continuo na linha.') """

nome = 'Bruno'
idade = 20

# formatação com format()
mensagem = 'Seu nome é {0} e sua idade é {1}'.format(nome, idade)
print(mensagem)

nome2 = 'John Marston'
idade2 = 34

#formatação com f-string
msg_f = f'Seu nome é {nome2} e sua idade é {idade2}'
print(msg_f)

a = b = 10
print(f'A soma de {a} com {b} é \'{a + b}\'')