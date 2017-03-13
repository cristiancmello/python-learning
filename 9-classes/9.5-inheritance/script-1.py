# Inheritance
class A:
    def __init__(self):
        self.name = 'A'

# B herda a classe A        
class B(A):
    pass

b = B()
print(b.name)   # A

class C(B):
    def __init__(self):
        self.name = 'C'

c = C()         # C
print(c.name)

# Função isinstance()
# Verifica a tipo de instância de um objeto.
print(isinstance(c, C)) # True
print(isinstance(c, B)) # True

# Função issubclass()
# Verifica a herança de uma classe
print(issubclass(B, A)) # B é subclasse de A? True.


# Herança Múltipla
class ClassA:
    def methodA(self):
        print('methodA()')
        
class ClassB:
    def methodB(self):
        print('methodB()')

class ClassC(ClassA,ClassB):
    pass

c = ClassC()
c.methodA()
c.methodB()