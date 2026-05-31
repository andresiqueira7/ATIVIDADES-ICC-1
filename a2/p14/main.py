def ordem(lista):
    crescente = sorted(lista)
    decrescente = sorted(lista, reverse=True)
    
    if lista == crescente:
        return "C"
    elif lista == decrescente:
        return "D"
    else:
        return "N"

a, b, c, d, e = map(int, input().split()) # o professor colocou entradas <13 mas tem entradas maiores. 
lista = [a, b, c, d, e] 

print(ordem(lista))