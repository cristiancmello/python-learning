# Strings
# Pode usar tanto '' quanto "" para expressar strings. Os caracteres de escape
# são POSIX (\n, \t, ...)

print('spam eggs')
print('\"Hello, Double Quotes\"')

print('Fist Line\n\tSecond Line.')

# String com caractere de formatação ignorado
print('Primeira linha\nova linha')  # Observa-se que 'nova linha' ficará 'ova linha'
print(r'Primeira linha\nova linha') # \n será ignorado

# Múltiplas linhas
print("""
Usage: stringify [OPTIONS]
    -json
    -JSON json
""")

# Concatenação (+) e Repetição (*)
print('ba' + 2 * 'na') # 'banana'

# Concatenação entre string literals
# IMPORTANTE! NÃO FUNCIONA ENTRE VARIÁVEIS OU EXPRESSÕES
print('Py' 'thon')     # 'Python'

# Concatenação entre string e variável
prefixo = 'Py'
print(prefixo + 'thon') # 'Python'

texto = ('Titulo'
        '\n\tTexto texto texto texto texto texto texto')
        
print(texto)

# Indexação de Strings
# Semelhante à linguagem C
word = 'Python'
print(word[0] + word[1] + word[2])    # Pyt

# Podemos obter caracteres da string de trás para frente
print(word[-3] + word[-2] + word[-1]) # hon

# IMPORTANTE! Índice 0 <=> -0
print(word[-0] + word[0]) # PP

# Slicing
# Com o Slicing, podemos subdividir a string em substrings
print(word[0:3])  # Pyt  ( intervalo: [0, 3) -> não inclui o índice 3 )
print(word[3:6])  # thon ( intervalo: [3, 6) -> não inclui o índice 6 )

# Equivalência
# String s = s[:i] + s[i:] (sempre tem início e exclui-se o fim)
print(word[:2])   # Py
print(word[2:])   # thon
print(word[:2] + word[2:]) # Python

# IMPORTANTE! 
#   - Valores fora de limite da string são tratados como região vazia da string
#   - Trechos de strings em Python não podem ser alterados - IMUTÁVEIS 
#        (qualquer tentativa de atribuição dará erro)

# Função len(s) (nativa, ou 'built-in')
# Equivalente ao strlen()
string = 'Lorem Ipsum'
print('Comprimento da string: ' + str(len(string)) + ' caracteres')

# printf-style
print("Name: %s\nAge: %d" % ('John Doe', 32))

# Alternativa
print('%(language)s' % {'language': 'Python'}) # Python