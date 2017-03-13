# Performance Measurement
# É interessante saber que o Python fornece funções para medida de performance
from timeit import Timer

print(Timer("mylist = [x for x in range(10)]").timeit())    # 0.796...
