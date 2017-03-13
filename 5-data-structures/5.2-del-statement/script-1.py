# del Statement
# Pode remove elemento de uma lista. A diferença em relação à função pop() é que
# o mesmo não retorna o elemento retirado.
# OBS.: PODE RETIRAR TRECHOS (SLICES) DE LISTAS
a = list(range(0, 5))

del a[0]
print(a)    # [1, 2, 3, 4]

del a[2:4]
print(a)    # [1, 2]

del a[:]
print(a)    # []

# Deletar variável
del a
print(a)    # lançará um erro, pois a variável foi "esvaziada"
