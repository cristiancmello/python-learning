# Handling Exceptions

import sys

def insert_number():
    while True:
        try:
            x = int(input('Por favor, insira um número: '))
            break
        except ValueError:
            print('Isso não é um número válido. Tente novamente.')

def open_file(filename: str):
    try:
        f = open(filename)
        num = int((f.readline()).strip())
    except OSError as err:
        print('OS Error: {0}'.format(err))
    except ValueError:
        print('Não é possível converter o dado em inteiro.')
    except:
        print('Error inesperado:', sys.exc_info()[0])
        raise
    
# Else clause
# É útil para o código que deve ser executado se a cláusula try capturar
# exceção.
def open_file2(filename: str):
    try:
        f = open(filename, 'r')
    except IOError:
        print('Não é possível abrir', filename)
    else:
        print(filename, 'tem', len(f.readlines()), 'linhas')

# raise
# Lançamento de uma exceção (instância de Exception)
def function1():
    try:
        raise Exception('spam', 'eggs')
    except Exception as inst:
        print(type(inst))
        print(inst.args)
        print(inst)
        
        x, y = inst.args    # unpack
        print('x =', x)
        print('y =', y)
        
def raising_exceptions():
    raise NameError("I'am Exception")
    
def raise_except():
    try:
        raising_exceptions()
    except NameError:
        print('Um exceção foi capturada!')
        raise   # dessa forma, não trata a exceção lançada

insert_number()
open_file('file1.txt')
open_file2('file1.txt')
function1()
raise_except()