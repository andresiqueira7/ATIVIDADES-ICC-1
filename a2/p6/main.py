n = int(input(''))
epitagorico = False

for a in range(n):
    for b in range (a, n):
      c = n - a - b

      if a > 1 and b > 1 and c > 1 and a*a + b*b == c*c:
            epitagorico = True
            print(a, b, c)
            break
      else:
            continue
if not epitagorico:
    print('Nao existe resposta')
