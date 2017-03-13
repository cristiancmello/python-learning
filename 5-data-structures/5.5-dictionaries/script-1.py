# Dictionaries
# São encontrados em outras linguagens como "arrays associativos".

emails = {'John': 'john@doe.com', 'Mary': 'mary@email.com'}
print(emails)   # {'John': 'john@doe.com', 'Mary': 'mary@email.com'}

# Podemos utilizar também o construtor 'dict'
emails = dict([('John', 'john@doe.com'), ('Mary', 'mary@email.com')])
print(emails)   # {'John': 'john@doe.com', 'Mary': 'mary@email.com'}

# Dict Comprehensions
names = {'name' + str(x): 'othername' + str(x) for x in (1, 2, 3)}
print(names)    # {'name2': 'othername2', 'name3': 'othername3', 'name1': 'othername1'}

# Podemos especificar as chaves em dict()
print(dict(name='John Doe', email='john@doe.com'))  # {'email': 'john@doe.com', 'name': 'John Doe'}
