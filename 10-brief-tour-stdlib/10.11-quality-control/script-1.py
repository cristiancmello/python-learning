# Quality Control
# Módulo 'doctest' auxilia na obtenção de funções para facilitar
# o desenvolvimento orientado a testes (TDD).
def getstring(name):
    """Retorna uma string com uma frase.
    
    >>> print(getstring('John Doe'))
    Hello, John Doe!
    """
    return 'Hello, {0}!'.format(name)
    
import doctest
print(doctest.testmod())    # TestResults(failed=0, attempted=1)

# O problema de se usar o módulo doctest é que a compreensão de um conjunto de testes
# fica menos legível. O módulo 'unittest' pode facilitar isso.

import unittest

class TestMyFunctions(unittest.TestCase):
    def test_getstring(self):
        self.assertEqual(getstring('John Doe'), 'Hello, JohSn Doe!')
        
unittest.main()

# OUTPUT
# AssertionError: 'Hello, John Doe!' != 'Hello, JohSn Doe!'
# - Hello, John Doe!
# + Hello, JohSn Doe!
# ?           +


# ----------------------------------------------------------------------
# Ran 1 test in 0.001s

# FAILED (failures=1)