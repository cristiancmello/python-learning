# Tuples and Sequences
# TIPOS DE DADOS SEQUENCIAIS => list, tuple, range
# Há um outro tipo sequencial => TUPLA
tupla = 2, 5, 'hello'   # ou (2, 5, 'hello')
print(tupla)    # (2, 5, 'hello')

# Suportam Nested Tuples
tupla = 1, 2, ('hello', 'world')
print(tupla)    # (1, 2, ('hello', 'world'))

# IMPORTANTE!
# TUPLAS SÃO IMUTÁVEIS, ASSIM COMO STRINGS.
# NO ENTANTO, PODEM CONTER OBJETOS MUTÁVEIS.
# tupla[0] = 'a'  # Erro...

v = ([1, 2, 3], [3, 2, 1])
print(v)          # ([1, 2, 3], [3, 2, 1])

# É possível essa construção...
empty = ()
singleton = 'hello',

print(len(empty), '=>', empty)           # 0 => ()
print(len(singleton), '=>', singleton)   # 1 => ('hello',)