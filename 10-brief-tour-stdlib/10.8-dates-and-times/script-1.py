# Dates and Times
# O módulo 'datetime' fornece classes para manipulação de datas de maneira simples.
from datetime import date
import math

# Calcular idade
now = date.today()
print(now)  # 2017-03-13

birthday = date(1994, 3, 27)
idade = now - birthday
print(math.floor(idade.days / 365)) # 22