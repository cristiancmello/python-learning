# Sets
# Pyhon inclui um tipo de dado chamado de 'sets'. Um set é uma coleção NÃO-ORDENADA
# SEM ELEMENTOS DUPLICADOS.
# OBS.: SEMELHANTE AO 'CONJUNTO' EM MATEMÁTICA
# OPERAÇÕES: union, intersection, difference e symmetric difference

basket = {'apple', 'orange', 'apple'}
print(basket)   # {'orange', 'apple'}

# Testar a presença de um elemento
print('apple' in basket)    # True

# Demonstração de operações
a = set('banana')
b = set('caqui')

print(a)        # {'a', 'b', 'n'}
print(b)        # {'u', 'a', 'i', 'c', 'q'}

print(a - b)    # Diferença: {'n', 'b'}
print(a | b)    # União: {'n', 'i', 'q', 'b', 'u', 'c', 'a'}
print(a & b)    # Interseção: {'a'}
print(a ^ b)    # Diferença simétrica: {'c', 'u', 'i', 'b', 'q', 'n'}

# Utilizando-se list comprehensions em sets
a = {x for x in 'abracadabra' if x not in 'abc'}

# 'abracadabra' <=> {'a', 'b', 'r', 'd'}
# 'abc'         <=> {'a', 'b', 'c'}

print(a)        # {'d', 'r'}
