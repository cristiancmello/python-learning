# User-defined Exceptions
# Podemos criar nossas próprias classes de exceção.

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)

def raising_my_exception():
    try:
        raise MyError(2*2)
    except MyError as err:
        print('Minha exceção ocorreu, value:', err.value)
        
raising_my_exception()