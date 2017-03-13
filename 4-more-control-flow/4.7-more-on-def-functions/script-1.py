# More on Defining Functions

# Valores-padrão em argumentos
def ask_ok(prompt, complaint="Sim ou não, por favor!"):
    while True:
        ok = input(prompt)
        if ok in ('sim', 's'):
            return True
        if ok in ('nao', 'n'):
            return False
        else:
            raise OSError('Entrada inválida')
        print(complaint)
        
# ask_ok('Deseja prosseguir?')

# Valor-padrão pode obter valor de uma variável declarada no escopo mais externo anterior
i = 5

def function(arg = i):
    print(arg)
    
i = 6
function()      # mostrará '5', pois obteve arg obteve o valor de i na def. da função

# É possível acumular os argumentos passados em chamadas subsequentes à função
def f(a, L = []):
    L.append(a)
    
    return L

print(f(1)) # [1]
print(f(2)) # [1, 2]
print(f(3)) # [1, 2, 4]

# Se não quiser reaproveitar o argumento das chamadas subsequentes, faça...
def f1(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
    
print(f1(1))    # [1]
print(f1(2))    # [2]
print(f1(3))    # [3]

# Keyword arguments
# Possuem a forma "kwarg=value"

def hello(msg, name="John Doe"):
    print(msg, name)

hello('Hello, World!', name='Laurence') # Hello, World! Laurence
hello('Hello, World!') # Hello, World! John Doe

# Parâmetro formal para receber Dictionary
def listar(first, *args):
    print('First argument: ', first)
    for arg in args:
        print(arg)

listar('John', 'Mary', 'Laurence')

# OUTPUT
# First argument:  John
# Mary
# Laurence

def listar_args(**args):
    # Imprimir keys
    for arg in args:
        print(arg)
        
    keys = sorted(args.keys())
    for k in keys:
        print(k, ':', args[k])
        
listar_args(name='John', lastname='Doe')

# OUTPUT
# name
# lastname
# lastname : Doe
# name : John

# IMPORTANTE!
# '*arg' deve ocorrer antes de '**args'

# Arbitrary Argument Lists
def concat(*args, sep='/'):
    return sep.join(args)
    
print(concat('earth', 'mars', 'venus'))             # earth/mars/venus
print(concat('earth', 'mars', 'venus', sep='.'))    # earth.mars.venus

# Unpacking Argument List
# 'Desempacotar' uma lista. Queremos transformar uma lista ou tupla em sequencia
# de argumentos a serem passados para uma função.
numeros = [1, 5, 1]
print(list(range(*numeros))) # equivale a list(range(1, 5, 1))

# A mesma regra vale para Dictionaries
usuario = {'name': 'John Doe', 'email': 'john@doe.com'}

def cadastrarUsuario(name, email):
    print(name, end='; ')
    print(email)
    
cadastrarUsuario(**usuario) # equivale a cadastrarUsuario(name='...', email='...')

# Expressões lambdas
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(10)
print(str(f(0)) + '\n' + str(f(1)))

# OUTPUT
# 10
# 11

# Functions Annotations
def function(arg1: str, arg2: int = 2) -> str:
    print('Annotations:', function.__annotations__)
    return arg1 + ' = ' + str(arg2)

print(function('param'))    # param = 2

# OUTPUT
# Annotations: {'return': <class 'str'>, 'arg1': <class 'str'>, 'arg2': <class 'int'>}
# param = 2
