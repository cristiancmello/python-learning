# String Pattern Matching
# Um módulo chamado 're' fornece ferramentas para processamento avançado de strings
# através de expressões regulares.
import re
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))  # ['foot', 'fell', 'fastest']

print('tea for too'.replace('too', 'two')) # tea for two