import math

def eh_quadrado_perfeito(n):
    raiz = int(math.sqrt(n))
    return raiz * raiz == n 

T = int(input())
resultados = []

for _ in range(T):
    n = int(input())
    hastes = [0] * n
    bola = 1

    while True:
        colocada = False
        for i in range(n):
          if hastes[i] == 0 or eh_quadrado_perfeito(hastes[i] + bola):
            hastes[i] = bola
            colocada = True
            break
   
        if not colocada:
          resultados.append(bola - 1)
          break
        bola += 1
        
for resultado in resultados:
    print(resultado)
    