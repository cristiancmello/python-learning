# Predefined Clean-up Actions
# Alguns objetos define ações que simplificam operações quando algo não está mais
# disponível.

def open_file(filename):
    for line in open(filename):
        print(line, end="")
    else:
        print('')

def open_file_2(filename):
    with open('file2.txt') as f:
        for line in f:
            print(line, end="")
        else:
            print('')
    
open_file('file1.txt')

# OUTPUT:
# banana
# maçã
# abacaxi

open_file_2('file2.txt')

# OUTPUT:
# line1
# line2
# line3