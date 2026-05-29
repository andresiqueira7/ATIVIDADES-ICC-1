import sys


def verificartriangulo(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return tipotriangulo(a, b, c)
        
    else:
        return "ALARME" 
        
def tipotriangulo(a, b, c):
    if a == b == c:
        return "VENDA"
    elif a == b or b == c or a == c:
        return "AJUSTE"
    else:
        return "AJUSTE"
      
while True:
    try:
        a, b, c = map(int, input().split())
        resultado = verificartriangulo(a, b, c)
        print(resultado)
        
        if resultado == "ALARME":
           sys.exit()
           
    except ValueError:
        sys.exit()
        
    except EOFError:
        sys.exit()