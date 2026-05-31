# Lê n e m na mesma linha
n, m = map(int, input().split())

matriz = []

# Lê a matriz de adjacência
for i in range(n):
    linha = list(map(int, input().split()))
    matriz.append(linha)

# Lista para anotar quais computadores já visitamos
# Usamos um 'set' (conjunto) porque é mais rápido para buscas
visitados = set()

# Uma lista que funcionará como a nossa "pilha" de tarefas.
# Vamos começar a explorar a rede a partir do computador 0.
pilha = [0]
visitados.add(0) # Marca o 0 como visitado

# Enquanto houver computadores na nossa pilha para explorar
while pilha:
    # Pega o computador atual
    atual = pilha.pop()
    
    # Olha para todos os outros computadores para ver se têm conexão
    for vizinho in range(n):
        # Se tem conexão (1) e a gente AINDA NÃO visitou esse vizinho
        if matriz[atual][vizinho] == 1 and vizinho not in visitados:
            visitados.add(vizinho) # Marca como visitado
            pilha.append(vizinho)  # Adiciona na pilha para explorar os contatos dele depois

# Se a quantidade de computadores que conseguimos visitar for igual ao total de computadores (n),
# significa que a rede inteira está conectada!
if len(visitados) == n:
    print("SIM")
else:
    print("NAO")