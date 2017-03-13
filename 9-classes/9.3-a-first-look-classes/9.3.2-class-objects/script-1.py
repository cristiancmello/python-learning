# Class Objects
class MyClassA:
    """Uma simples classe de exemplo"""
    i = 12345
    
    def f(self):
        return 'Hello, World!'

# Instanciação
x = MyClassA()

# Chamada à função do objeto
print(x.f())    # Hello, World!
print(x.i)      # 12345

class MyClassB:
    # Ao se invocar o construtor da classe, o método abaixo será executado
    # Obs.: 'self' <=> 'this' em outras linguagens
    # IMPORTANTE!
    # 'self' É OBRIGATÓRIO DENTRO DAS CLASSES!!!
    def __init__(self):
        self.data = ['elem1']

x = MyClassB()
print(x.data[0])    # elem1

class MyClassC:
    # Constructor
    def __init__(self, arg1, arg2):
        print('{0}, {1}'.format(arg1, arg2))
        
x = MyClassC('lala', 'nana')    # lala, nana
