nome = 'Bruno'
sobrenome = 'Manganoti'
# letra = nome[2]
# print(letra)

""" print(len(nome))

print(nome + ' ' + sobrenome)

frase = 'um dois três quatro.'
palavras = frase.split() """

""" for letra in frase:
    print(letra) """

# print(frase[0:5])

""" email = input('Digite seu email: ')
arroba = email.find('@')

usuario = email[0:arroba]
dominio = email[arroba+1:]

print(usuario)
print(dominio)

print('brunomanganoti' in email) """

""" item = 'hipoclorito'

pos = item.find('clor')
print(pos)

pos = item.find('flu')
print(pos) """

""" objeto_celeste = 'galáxia esPiral M31'

print(objeto_celeste.upper())
print(objeto_celeste.capitalize())
print(objeto_celeste.title()) """

""" suplemento = 'cloreto de magnésio'
n_suplemento = suplemento.replace('magnésio', 'zinco')

print(suplemento)
print(n_suplemento) """

""" frase = '    frase     teste   !  !  !  '
print(frase)

frase_esq = frase.lstrip()
frase_dir = frase.rstrip()
frase_corte = frase.strip()
print(frase_esq)
print(frase_dir)
print(frase_corte) """

""" fruta = 'Abacate'
print(fruta)
print(fruta.rjust(20))
print(fruta.ljust(20, "-"))
print(fruta.center(20, "-")) """

""" p = 'Betoneira training'
print(p.startswith('Be')) # true
print(p.startswith('Bo')) # false
print(p.endswith('g'))    # true
print(p.endswith('ng'))   # true
print(p.endswith('eg'))   # false """

# Docstrings
texto = """
Docstring é uma espécie de documentação
que podemos inserir dentro de um módulo, função
ou classe no Python, entre outros locais.
    Respeita deslocamento do texto e é multilinhas.
"""
print(texto)