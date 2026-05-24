import math

n = int(input())

valores = list(map(float, input('').split()))
media = sum(valores) / n
variancia = sum((x - media) ** 2 for x in valores) / n
desvio_padrao = math.sqrt(variancia)
print(f'{desvio_padrao:.4f}')
 