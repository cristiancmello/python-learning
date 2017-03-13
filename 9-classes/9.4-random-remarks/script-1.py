# Random Remarks

# Podemos definir uma função for do contexto sintático de uma classe
def f1(self, x, y):
    return min(x, x+y)
    
class C:
    f = f1
    def g(self):
        return 'Hello, World!'
    h = g
    
c = C()
print(c.f(4, 1))
print(c.h())