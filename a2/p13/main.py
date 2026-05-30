
def MDC(x, y):
  if y == 0:
    return x
  else:
    return MDC(y, x % y)
  
a = int(input())
while a < 1 or a > 1000:
  a = int(input())
  
b = int(input())
while b < 1 or b > 1000:
  b = int(input())
  
resultado = MDC(a, b)
print(resultado)
