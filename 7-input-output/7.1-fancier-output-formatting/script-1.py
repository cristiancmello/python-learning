# Fancier Output Formatting
s = 'Hello, World!'
print(str(s))       # Hello, World!

# Exibir a representação do Python para a estrutura de dados
print(repr(s))      # 'Hello, World!'

print(repr('Hello, World!\n'))  # 'Hello, World!\n'

# Representação de tupla
print(repr((10, 12, ('spam', 'spam2'))))    # (10, 12, ('spam', 'spam2'))

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))

for x in range(1, 11):
    print('{0:02} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
    
# OUTPUT:
# 01   1    1
# 02   4    8
# 03   9   27
# 04  16   64
# 05  25  125
# 06  36  216
# 07  49  343
# 08  64  512
# 09  81  729
# 10 100 1000

# Função str.zfill()
# Preenche com zeros à esquerda até o limite especificado.
print('12'.zfill(5))    # 00012

# Função str.format()
print('My name is {name}!'.format(name='John Doe'))     # My name is John Doe!

table = {'John': 1230, 'Jack': 4334}
print('Jack: {0[Jack]:d}; John: {0[John]:d}'.format(table))

# Podemos fazer dessa form também
print('Jack: {Jack:d};'.format(**table))

