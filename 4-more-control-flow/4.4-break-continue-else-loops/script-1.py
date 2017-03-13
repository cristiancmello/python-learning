# Break, continue and else Clauses on Loops
# Break e continue possuem o mesmo comportamento que em C.

# Else clause on Loop: permite que se faça alguma ação após o fim do loop
for i in range(3):
    print(i)
else:
    print("Nenhum item a mais.")
    
# 0
# 1
# 2
# Nenhum item a mais.

# Verificar números primos e múltiplos no intervalo [2, 10)
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, ' is a prime number')