n = int(input())
epitagorico = False

for a in range(1, n):
    for b in range(a, n):
        c = n - a - b
        
        if c > 0 and (a*a + b*b == c*c):
            print(a, b, c)
            epitagorico = True
            break  
    
    if epitagorico:
        break

if not epitagorico:
    print('Nao existe resposta')
    