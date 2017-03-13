# Defining Functions
# Palavra 'def' introduz a definição de uma função

def hello():
    print('Hello, World!')
    
hello() # 'Hello, World!'

# DOCSTRING
# A primeira linha da definição da função pode ter string de comentário para ducumentação
def my_function():
    """
    my_function: função
    RETURN: None
    """
    pass

# Imprimir na tela a doc. da função
print(my_function.__doc__)

# IMPORTANTE!
# Interpretador reconhece funções de usuári como sendo 'user-defined'.

# Imprimir na tela metadados da função em memória
print(my_function)  # algo assim "<function my_function at 0x7f945032e0d0>"

# Pode-se atribuir a uma variável a função
f = my_function
print(f()) # None (função sem retorno explícito irá retornar 'None')

def number():
    return -1

num = number
print(num()) # -1