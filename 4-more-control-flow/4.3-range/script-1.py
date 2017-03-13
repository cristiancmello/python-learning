# Função range()
# Gera uma progressão aritmética

for i in range(5):
    print(i)

print('\n')

# OUTPUT:
# 0
# 1
# 2
# 3
# 4

for i in range(5, 10):
    print(i)

print('\n')

# OUTPUT:
# 5
# 6
# 7
# 8
# 9

# Range com saltos pares (incrementos de 2 em 2)
for i in range(0, 10, 2):
    print(i)
    
# OUTPUT:
# 0
# 2
# 4
# 6
# 8

# Utilizar range() e len() juntos
names = ['John', 'Mary', 'Laurence']
for i in range(len(names)):
    print(i, names[i])

# OUTPUT:  
# 0 John
# 1 Mary
# 2 Laurence

# Função list() para iterar sobre uma lista de inteiros
print(list(range(3)))  # [0, 1, 2]
