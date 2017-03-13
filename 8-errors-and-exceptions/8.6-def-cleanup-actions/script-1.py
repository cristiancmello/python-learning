# Defining Clean-up Actions
# Bloco try tem uma outra cláusula opcional que deverá ser executada 
# em qualquer circunstância.

# try:
#     raise KeyboardInterrupt
# finally:
#     print('Goodbye, world!')
    
# OUTPUT
# Goodbye, world!
# Traceback (most recent call last):
#   File "script-1.py", line 6, in <module>
#     raise KeyboardInterrupt
# KeyboardInterrupt

# Cláusula else seguida por finally
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('Divisão por Zero!')
    else:
        print('Resultado =', result)
    finally:
        print('Executando cláusula finally')

divide(1, 0)

# OUTPUT
# Divisão por Zero!
# Executando cláusula finally