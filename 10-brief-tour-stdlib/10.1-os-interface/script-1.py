# Operating System Interface

# Função getcwd()
# Retorna a pasta corrente de trabalho.
import os
print(os.getcwd())  # /home/...

# Função system()
# Executa comando do sistema.
os.system('touch file-1.txt')   # criação de arquivo na pasta corrente
