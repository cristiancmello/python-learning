# Error Output Redirection and Program Termination
# O módulo sys possue atributos como os streams stdin, stdout e stderr.

# Emitir um stream de erro
import sys
sys.stderr.write('Falha ao abrir o arquivo.\n') # Falha ao abrir o arquivo.
