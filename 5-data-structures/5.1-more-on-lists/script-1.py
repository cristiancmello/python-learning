# Data Structures
# Funções de listas

# Append
# Colocar um elemento ao final de uma lista.
lista = [1, 2]
lista.append(3)
print(lista)    # [1, 2, 3]

# Extend
# Colocar uma lista ao final de outra.
lista = [1, 2]
lista.extend([3, 4])
print(lista)    # [1, 2, 3, 4]

# Insert
# Inserir um elemento em determinada posição.
lista.insert(0, 5)
print(lista)    # [5, 1, 2, 3, 4]

# Remove
# Remover o primeiro item da lista.
lista.remove(5)
print(lista)    # [1, 2, 3, 4]

# Pop
# Remove elemento da lista e o retorna.
print(lista.pop()) # 4
print(lista)       # [1, 2, 3]

# Podemos especificar o índice.
print(lista.pop(1))
print(lista)       # [1, 3]

# Clear
# Remove todos os itens de uma lista. Equivale a 'del a[:]'.
lista.clear()
print(lista)

# Index
# Retorna o índice do primeiro elemento encontrada na lista.
lista = [1, 2, 3]
print(lista.index(2))   # 1

# Sort
# Ordena uma lista.
lista = [-1, 5, 4, 2, 1, 0]
lista.sort()
print(lista)    # [-1, 0, 1, 2, 4, 5]

# Reverse
# Reverte os elementos da lista
lista.reverse()
print(lista)    # [5, 4, 2, 1, 0, -1]

# Copy
# Retorna uma cópia da lista.
lista_copia = lista.copy()
print(lista_copia)

# IMPORTANTE!
# Podemos utilizar as listas como pilhas também.

# Usando Listas como Filas
# Importar 'deque', que possui funcionalidades de fila
from collections import deque
fila = deque(['John', 'Eric', 'Michael'])

# Colocar 'Terry' ao final da fila
fila.append('Terry')

# O primeiro da fila será "atendido". Ou seja, 'John' será atendido
fila.popleft()
print(fila)     # deque(['Eric', 'Michael', 'Terry'])

# List Comprehensions
# Provê uma forma concisa de criar listas.

squares = []
for x in range(10):
    squares.append(x**2)

print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Podemos escrever de forma concisa...
#    {x pertence a [0, 1, 2, ..., 9] | x**2}
# ou {x**2 | x pertence a [0, 1, 2, ...., 9]}
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Alternativa usando Expressão Lambda
squares = list(map(lambda x: x**2, range(10))) # funcao => lambda x x**2 (entrada de x)
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Podemos fazer estruturas mais elaboradas
# { par (x, y) na lista | Para todo x e y pertencente a [1, 2, 3] e [3, 1, 4] ^ x != y }
lista = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(lista)

# Operação de flatten numa matriz
matriz = [[1, 2, 3], [4, 5, 6]]
flatten_matriz = [num for elem in matriz for num in elem]
print(flatten_matriz)   # [1, 2, 3, 4, 5, 6]

# Nested function in List Comprehension
from math import pi
lista_pi_prec = [str(round(pi, i)) for i in range(1, 4)]
print(lista_pi_prec)    # ['3.1', '3.14', '3.142']

