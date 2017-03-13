# Executing modules as scripts

def welcome(name='John Doe'):
    print('Hello,', name, end='!\n')

# Ao final do módulo, após a chamada por CLI, __name__ é setado como "__main__"
if __name__ == "__main__":
    import sys
    welcome(sys.argv[1])
    
# IMPORTANTE! 
# Se o código com a "função main()" for importado, o mesmo não será
# executado se for importado. Isso é conveniente para interface de usuário
# ou propósitos de testes (rodando o módulo como um script que executa testes)
