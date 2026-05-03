N = int(input(''))
while (N < 1 or N > 1000): 
    N = int(input(''))
    
lista = []
    
for i in range(N):
    numero = int(input(''))
    if numero < (-100) or numero > 100:
        numero = int(input(''))    

    lista.append(numero)
    
contador = 0
i = 0

while i < N - 2:
    r = lista[i+1] - lista[i]
    j = i + 1 
    while j < N - 1 and lista[j + 1] - lista[j] == r:
        j += 1
    if j - i >= 1:
        contador += 1
    i = j 
    
print(contador)