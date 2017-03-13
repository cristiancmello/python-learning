# Mathematics
# O módulo de 'math' fornece acesso à biblioteca padrão de matemática em C
# para matemática de p.f.
import math

print(math.cos(math.pi / 4))    # 0.7071067811865476

# Módulo random
# Provê funcionalidades de geração de padrões pseudo-aleatórios.
import random
print(random.choice(['banana', 'maçã', 'uva'])) # banana | maçã | uva

# Função sample()
# Geração de amostras
print(random.sample(range(100), 10))    # Ex.: [91, 33, 80, 81, 26, 3, 13, 24, 11, 46]

# Módulo statistics
# Fornece funções da estatística
import statistics
data = [10, 4, 3, 5, 6, 8]

# Tirar a média
print(statistics.median(data))  # 5.5
