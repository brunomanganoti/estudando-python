# Tuplas são imutáveis

# tupla = (2,3,9,18)
# print(tupla)

halogenios = ('F', 'Cl', 'Br', 'I', 'At')

gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')

concat = halogenios + gases_nobres

# t1 = (1,9,2,2,4,4,345,6,6,4,45,6,7,89,5,4,3,32,)
print('Cl' in halogenios) # true
print('Cl' in concat)     # true
print('Fe' in concat)     # false

""" Operações não disponíveis em tuplas: 
    - sort 
    - append
    - reverse """

grupo1 = ['Li', 'Na', 'K', 'Cs']

alcalinos = tuple(grupo1)

print(sorted(alcalinos))