# Obter série de Fibonacci
a, b = 0, 1

while b < 10:
    print(b)
    (a, b) = (b, a+b)  # a=b, b=a+b
    
i = 256 * 256
print('i = ', i)

a, b = 0, 1
while b < 10:
    print(b, end=',')  # end => omite '\n' e finaliza string com expressão
    a, b = b, a+b
    