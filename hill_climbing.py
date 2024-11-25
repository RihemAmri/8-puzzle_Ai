import random

class HillClimbingSolver:
    @staticmethod
    def solve_puzzle(initial_state, goal_state, max_iterations=1000, max_restarts=100):
        def heuristic(state):
            return sum(state[i][j] != goal_state[i][j] for i in range(3) for j in range(3))
        
        def get_neighbors(state):
            neighbors = []
            empty_tile = [(i, j) for i in range(3) for j in range(3) if state[i][j] == 0][0]
            i, j = empty_tile
            moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for move in moves:
                ni, nj = i + move[0], j + move[1]
                if 0 <= ni < 3 and 0 <= nj < 3:
                    new_state = [list(row) for row in state]
                    new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
                    neighbors.append(tuple(map(tuple, new_state)))
            return neighbors
        
        def hill_climbing(state):
            current_state = state
            current_cost = heuristic(current_state)
            iterations = 0
            while iterations < max_iterations:
                neighbors = get_neighbors(current_state)
                next_state = min(neighbors, key=heuristic)
                next_cost = heuristic(next_state)
                if next_cost >= current_cost:
                    break
                current_state, current_cost = next_state, next_cost
                iterations += 1
                if current_state == goal_state:
                    return [current_state], iterations
            return current_state, iterations

        def generate_random_state():
            numbers = list(range(9))
            random.shuffle(numbers)
            state = [numbers[i:i+3] for i in range(0, 9, 3)]
            return tuple(map(tuple, state))

        for restart in range(max_restarts):
            current_state, iterations = hill_climbing(initial_state)
            if current_state == goal_state:
                solution_path = [current_state]
                while iterations > 0:
                    neighbors = get_neighbors(current_state)
                    current_state = min(neighbors, key=heuristic)
                    solution_path.append(current_state)
                    iterations -= 1
                return solution_path, iterations
            initial_state = generate_random_state()
        
        return [], max_iterations

if __name__ == "__main__":
    initial_state = ((7, 2, 4), (5, 0, 6), (8, 3, 1))
    goal_state = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
    solution, iterations = HillClimbingSolver.solve_puzzle(initial_state, goal_state)
    if solution:
        print("Solution found in", iterations, "iterations:")
        for step in solution:
            for row in step:
                print(row)
            print("-------------")
    else:
        print("No solution found.")
