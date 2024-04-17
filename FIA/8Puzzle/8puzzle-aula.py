def heuristic(state, goal):
    # Calcula a distância de Manhattan para heurística
    distance = 0
    for i in range(len(state)):
        if state[i] != 0:
            distance += abs(state[i] // 3 - goal.index(state[i]) // 3) + abs(state[i] % 3 - goal.index(state[i]) % 3)
            # em python //
            # divisão inteira: por exemplo 7 // 3 resulta em 2, porque? 2.333 ou seja 2
            # em python %¨
            # módulo: por exemplo 5 % 3 resulta em 2, porque? sobra 2
    return distance

def get_neighbors(state):
    # Obtém todos os estados vizinhos válidos a partir do estado atual
    neighbors = []
    zero_index = state.index(0)
    if zero_index + 3 < 9:  # Mover o espaço para baixo
        neighbors.append(swap_positions(state, zero_index, zero_index + 3))
    if zero_index - 3 >= 0:  # Mover o espaço para cima
        neighbors.append(swap_positions(state, zero_index, zero_index - 3))
    if zero_index % 3 < 2:  # Mover o espaço para a direita
        neighbors.append(swap_positions(state, zero_index, zero_index + 1))
    if zero_index % 3 > 0:  # Mover o espaço para a esquerda
        neighbors.append(swap_positions(state, zero_index, zero_index - 1))
    return neighbors

def swap_positions(state, i, j):
    # Troca as posições i e j no estado
    new_state = list(state)
    new_state[i], new_state[j] = new_state[j], new_state[i]
    return tuple(new_state)


# BUSCA DO CAMINHO COM A-STAR
def a_star(initial, goal):
    # Implementação do algoritmo A* sem utilizar PriorityQueue
    open_set = [(heuristic(initial, goal), initial)]  # Lista de estados abertos
    came_from = {initial: None}
    g_score = {initial: 0}
    
    while open_set:
        # Ordena e obtém o estado com menor f_score
        open_set.sort(key=lambda x: x[0])
        current = open_set.pop(0)[1]

        if current == goal:
            return reconstruct_path(came_from, initial, current)

        for neighbor in get_neighbors(current):
            tentative_g_score = g_score[current] + 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                open_set.append((f_score, neighbor))
    return []




def reconstruct_path(came_from, start, goal):
    # Reconstrói o caminho de start até goal
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path

# Estados inicial e final do puzzle
initial = (1, 0, 3, 4, 2, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Encontra o caminho da solução usando A*
solution_path = a_star(initial, goal)
print(solution_path)