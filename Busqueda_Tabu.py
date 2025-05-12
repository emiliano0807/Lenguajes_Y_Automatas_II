def tabu_search(initial_solution, cost_function, neighbor_function, iterations=100, tabu_size=10):
    current_solution = initial_solution[:]
    best_solution = current_solution[:]
    best_cost = cost_function(current_solution)
    tabu_list = []

    for _ in range(iterations):
        neighbors = neighbor_function(current_solution)
        neighbors = sorted(neighbors, key=lambda x: cost_function(x[0]))

        for neighbor, move in neighbors:
            if move not in tabu_list:
                current_solution = neighbor
                current_cost = cost_function(current_solution)

                if current_cost < best_cost:
                    best_solution = current_solution
                    best_cost = current_cost

                tabu_list.append(move)
                if len(tabu_list) > tabu_size:
                    tabu_list.pop(0)
                break  # solo aceptamos el primer vecino no tabú

    return best_solution, best_cost
