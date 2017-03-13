# Reading and writing files

# Função open()
# Abri um arquivo em formato de texto
f = open('file1.txt', 'r')

# Ler o arquivo e mostrar conteúdo na tela
print(f.read()) # Hello, World!
print(f.read()) # SEM CONTEÚDO (POSIÇÃO DE LEITURA É ALTERADA)

# Função close()
# Encerra o arquivo, liberando recursos.
f.close()

# Função readline()
# Ler uma linha inteira até o caractere '\n'.
f = open('file2.txt', 'r')
print(f.readline(), end='') # Banana
print(f.readline(), end='') # Maçã
f.close()

# Função de leitura tratada (semelhante usando try-finally)
with open('file2.txt', 'r') as f:
    read_data = f.read()
    print(read_data)
f.closed

# OUTPUT:
# Banana
# Maçã
# Romã

# Salvando estrutura de dados com JSON
# É muito comum termos problemas de complexidade ao se criar formatos de dados
# próprios para transacionar entre as aplicações. O Python trouxe funcionalidades
# para se serializar estruturas em JSON (isto é, trazendo da mem. RAM para arquivo)
# e deserializar (trazer de um arquivo para estrutura em RAM).
import json

# Função dumps
# Serializar um objeto
j = json.dumps({'name': 'John Doe', 'tels': ['1234', '4321']})
print(j)    # {"tels": ["1234", "4321"], "name": "John Doe"}

# Função dump
# Serializar um objeto e salvá-lo um arquivo .json
f = open('file3.json', 'w')
json.dump({'name': 'John Doe', 'tels': ['1234', '4321']}, f)
f.close()

# Função load
# Carregar um arquivo .json e deseserializar
pessoa = json.load(open('file4.json', 'r'))
print(pessoa)   # {'name': 'Laurence', 'email': 'laurence@email.com'}
