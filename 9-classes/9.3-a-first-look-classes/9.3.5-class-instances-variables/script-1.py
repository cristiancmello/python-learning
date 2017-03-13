# Class and Instance Variables

# IMPORTANTE!
# O código abaixo poderá ter efeito indesejável.

class Dog:
    tricks = []
    
    def __init__(self, name):
        self.name = name
        
    def add_trick(self, trick):
        self.tricks.append(trick)
        
d, e = Dog('Fido'), Dog('Lulu')
d.add_trick('rolar')
e.add_trick('fingir de morto')

print(d.name + ' - tricks = ' + str(d.tricks)) # Fido - tricks = ['rolar', 'fingir de morto']
print(e.name + ' - tricks = ' + str(e.tricks)) # Lulu - tricks = ['rolar', 'fingir de morto']


# Percebe-se que objetos 'd' e 'e' compartilham uma mesma propriedade.
# Abaixo, está uma forma de tornar 'tricks' único para cada instância.

class Cat:
    def __init__(self, name):
        self.name = name
        self.tricks = []    # aloca dentro do construtor
        
    def add_trick(self, trick):
        self.tricks.append(trick)
        
b, c = Cat('Meow'), Cat('Tici')
b.add_trick('lamber pelo')
c.add_trick('cuspir pelos')

print(b.name + ' - tricks = ' + str(b.tricks)) # Meow - tricks = ['lamber pelo']
print(c.name + ' - tricks = ' + str(c.tricks)) # Tici - tricks = ['cuspir pelos']
