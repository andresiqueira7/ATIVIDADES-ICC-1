N = int(input(''))

while (N < 1 or N > 1000): 
    N = int(input(''))
    
sequencia = list(map(int, input().split()))

if N <= 2:
    print('1')
else:
    qtd_pas = 1
    razao_atual = sequencia[1] - sequencia[0]
    for i in range(2, N):
        razao = sequencia[i] - sequencia[i-1]
        if razao != razao_atual:
            qtd_pas += 1
            razao_atual = razao

    
    print(qtd_pas)
    