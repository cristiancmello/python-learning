# More on Modules

# Podemos importar variáveis e funções globais
from hello import hello, hello2

# Chamar funções do módulo
hello()
print(hello2('Laurence'))

# Importar todos os nomes do módulo
from hello import *
