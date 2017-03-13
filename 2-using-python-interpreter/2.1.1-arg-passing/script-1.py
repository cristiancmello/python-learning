import sys # importar modulo 'sys'

the_world_is_flat = True
if the_world_is_flat:
    print("Be careful not to fall off!")

# Mostrar argumentos de linha de comando (Modo Interativo)
# Passagem: python3 script-1.py arg1 arg2

# Mostrar todos os argumentos
print(sys.argv)

# Mostrar arg[0] e arg[1]
print(sys.argv[0] + sys.argv[1])
