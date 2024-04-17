from queue import PriorityQueue

def distanciaManhattan(estado, estadoFinal):
    distance = 0
    for i in range(len(estado)):
        for j in range(len(estado[i])):
            if estado[i][j] != estadoFinal[i][j]:
                x, y = divmod(estadoFinal[i][j] - 1, len(estado))
                distance += abs(x - i) + abs(y - j)
    return distance

def a_estrela(estado, estadoFinal):
    estado = tuple(tuple(x) for x in estado)
    estadoFinal = tuple(tuple(x) for x in estadoFinal)

    open_set = PriorityQueue() # fila de prioridade para os estados a serem avaliados
    open_set.put((0, estado))
    estadoAnterior = {}
    g_score = {estado: 0} # custo do caminho do estado inicial até o estado atual 
    f_score = {estado: distanciaManhattan(estado, estadoFinal)} # heuristica + custo do caminho do estado inicial até o estado atual
    
    while not open_set.empty():
        estadoAtual = open_set.get()[1]

        if estadoAtual == estadoFinal: 
            caminho = [] 
            while estadoAtual in estadoAnterior: 
                caminho.append(estadoAtual) 
                estadoAtual = estadoAnterior[estadoAtual]
            caminho.append(estado)
            caminho.reverse()
            return caminho

        for move in MovimentosPossiveis(estadoAtual): 
            novo_g_score = g_score[estadoAtual] + 1 
            if move not in g_score or novo_g_score < g_score[move]:
                estadoAnterior[move] = estadoAtual
                g_score[move] = novo_g_score
                f_score[move] = novo_g_score + distanciaManhattan(move, estadoFinal)
                open_set.put((f_score[move], move))
    return None


# Basicamente a mesma logicas dos vizinhos, com algumas alterações para o 8-puzzle com o manhattan

def MovimentosPossiveis(estado):
    moves = []
    i, j = estadoBranco(estado)
    if i > 0:
        moves.append(trocaEstados(estado, i, j, i - 1, j))
    if i < len(estado) - 1:
        moves.append(trocaEstados(estado, i, j, i + 1, j))
    if j > 0:
        moves.append(trocaEstados(estado, i, j, i, j - 1))
    if j < len(estado[0]) - 1:
        moves.append(trocaEstados(estado, i, j, i, j + 1))
    return moves


# Retorna a posição do espaço em branco, para descobrir os possiveis movimentos
def estadoBranco(estado):
    for i in range(len(estado)):
        for j in range(len(estado[i])):
            if estado[i][j] == 0:
                return i, j

def trocaEstados(estado, i1, j1, i2, j2):
    novoEstado = [list(x) for x in estado]  # converter tuplas para listas
    novoEstado[i1][j1], novoEstado[i2][j2] = novoEstado[i2][j2], novoEstado[i1][j1] # trocar os estados
    return tuple(tuple(x) for x in novoEstado)  # voltar listas para tuplas

# Execução
quadroFinal = [[1, 2, 3], 
               [4, 5, 6],
               [7, 8, 0]]

quadroInicial = [[5, 8, 0], 
                 [6, 4, 7], 
                 [2, 3, 1]]

caminho = a_estrela(quadroInicial, quadroFinal)
if caminho is not None:
    contador = 0
    print("Solução:")
    for estado in caminho:
        print(estado)
        contador += 1
    print("Total de passos: ", contador)
        
else:
    print("Solução não encontrada.")