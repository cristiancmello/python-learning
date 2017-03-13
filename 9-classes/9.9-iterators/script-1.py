# Iterators
# Muitos objetos podem ser percorridos por loops 'for'.

for element in [1, 2, 3]:
    print(element)

for element in (1, 2, 3):
    print(element)

for key in {'one': 1, 'two': 2}:
    print(key)
    
# Por trás da cortina, o Python chama o método 'iter()' do objeto.

obj = {'name': 'John Doe', 'email': 'john@doe.com'}

it = iter(obj)
print(next(it)) # name
print(next(it)) # email
