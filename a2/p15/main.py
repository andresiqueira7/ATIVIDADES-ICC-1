n = int(input())
matriz = []

for i in range(n):
    linha = list(map(int, input().split()))
    matriz.append(linha)

# Calcular somas
soma_linha = sum(matriz[0]) #
soma_coluna = sum(matriz[i][0] for i in range(n)) 
soma_diagonal_principal = sum(matriz[i][i] for i in range(n))
soma_diagonal_secundaria = sum(matriz[i][n-1-i] for i in range(n))

if soma_linha == soma_coluna == soma_diagonal_principal == soma_diagonal_secundaria:
    print(soma_linha)
else:    print("0")
