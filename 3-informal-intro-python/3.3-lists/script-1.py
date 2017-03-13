# Listas
lista = [1, 2, 4, 5, 8]
print(lista) # [1, 2, 4, 5, 8]

# Indexação e Slicing
print(lista[0])    # 1
print(lista[2:])   # [4, 5. 8]
print(lista[:])    # lista <=> lista[:] => [1, 2, 4, 5, 8]

# Concatenação
print(lista + [-2, -4])

# IMPORTANTE!
# Diferentemente das Strings, Listas SÃO MUTÁVEIS
lista[2] = 2 ** 3
print(lista)

# Função append()
# Coloca novos itens ao final da lista
lista.append(7 ** 3)
print(lista)

# Atribuição a slices
# É possível modificar o tamanho da lista ou apagá-la inteiramente
letters = ['a', 'b', 'c', 'd']
letters[1:3] = ['B', 'C']
print(letters)  # ['a', 'B', 'C', 'd']

# Remoção de itens
letters[1:3] = []
print(letters)  # ['a', 'd']

# Removendo todos os elementos
letters[:] = []
print(letters)

# Função len()
# Da mesma forma feita com Strings, é possível calcular comprimento da lista
letters = ['a', 'b', 'c', 'd']
print('Comprimento de letters = ' + str(len(letters)) + ' elementos')

# Definindo Nested Lists (Listas aninhadas)
A = [1, 2, 3]
B = [A, 5, 6, 7]
print(B) # [[1, 2, 3], 5, 6, 7]

C = [A, B]
print(C) # [[1, 2, 3], [[1, 2, 3], 5, 6, 7]]

# Mostrar por linha e coluna
print(C[0][2]) # 3

