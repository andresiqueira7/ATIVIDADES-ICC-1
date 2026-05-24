import math

def contar_primos_distintos(n):
    primos = set()
    d = 2
    temp = n
    while d * d <= temp:
        if temp % d == 0:
            primos.add(d)
            while temp % d == 0:
                temp //= d
        d += 1
    if temp > 1:
        primos.add(temp)
    return len(primos)
  
n = int(input())
        
k = contar_primos_distintos(n)

if k < 2:
    print(0)
else:
    resultado = (2 ** k) - k - 1
    print(resultado)
    