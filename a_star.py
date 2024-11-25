# from queue import PriorityQueue

# class AStarSolver:
#     @staticmethod
#     def solve_puzzle(initial_state, goal_state):
#         frontier = PriorityQueue()
#         frontier.put((0, initial_state))
#         came_from = {initial_state: None}
#         cost_so_far = {initial_state: 0}

#         while not frontier.empty():
#             current_cost, current_state = frontier.get()

#             if current_state == goal_state:
#                 # Reconstruct path
#                 path = []
#                 while current_state in came_from:
#                     path.insert(0, current_state)
#                     current_state = came_from[current_state]
#                 return path

#             for next_state in AStarSolver.get_neighbors(current_state):
#                 new_cost = cost_so_far[current_state] + 1
#                 if next_state not in cost_so_far or new_cost < cost_so_far[next_state]:
#                     cost_so_far[next_state] = new_cost
#                     priority = new_cost + AStarSolver.heuristic(next_state, goal_state)
#                     frontier.put((priority, next_state))
#                     came_from[next_state] = current_state

#         return None


#     @staticmethod
#     def get_neighbors(state):
#         neighbors = []
#         empty_tile_i, empty_tile_j = None, None
#         for i in range(3):
#             for j in range(3):
#                 if state[i][j] == 0:
#                     empty_tile_i, empty_tile_j = i, j

#         for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#             new_i, new_j = empty_tile_i + move[0], empty_tile_j + move[1]
#             if 0 <= new_i < 3 and 0 <= new_j < 3:
#                 new_state = [list(row) for row in state]
#                 new_state[empty_tile_i][empty_tile_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[empty_tile_i][empty_tile_j]
#                 neighbors.append(tuple(map(tuple, new_state)))

#         return neighbors

#     @staticmethod
#     def heuristic(state, goal_state):
#         # Manhattan distance heuristic
#         distance = 0
#         for i in range(3):
#             for j in range(3):
#                 if state[i][j] != goal_state[i][j] and state[i][j] != 0:
#                     x, y = divmod(goal_state[i][j], 3)
#                     distance += abs(x - i) + abs(y - j)
#         return distance


from queue import PriorityQueue

class AStarSolver:
    @staticmethod
    def solve_puzzle(initial_state, goal_state):
        
        frontier = PriorityQueue()
        frontier.put((0, initial_state))
        came_from = {initial_state: None}
        cost_so_far = {initial_state: 0}
        iterations = 0

        while not frontier.empty():
            _, current_state = frontier.get()
            iterations += 1

            if current_state == goal_state:
                # Reconstruct path
                path = []
                while current_state in came_from:
                    path.insert(0, current_state)
                    current_state = came_from[current_state]
                return path, iterations

            for next_state in AStarSolver.get_neighbors(current_state):
                new_cost = cost_so_far[current_state] + 1
                if next_state not in cost_so_far or new_cost < cost_so_far[next_state]:
                    cost_so_far[next_state] = new_cost
                    priority = new_cost + AStarSolver.heuristic(next_state, goal_state)
                    frontier.put((priority, next_state))
                    came_from[next_state] = current_state

        return None, iterations

    @staticmethod
    def get_neighbors(state):
        neighbors = []
        empty_tile_i, empty_tile_j = None, None
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    empty_tile_i, empty_tile_j = i, j

        for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_i, new_j = empty_tile_i + move[0], empty_tile_j + move[1]
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_state = [list(row) for row in state]
                new_state[empty_tile_i][empty_tile_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[empty_tile_i][empty_tile_j]
                neighbors.append(tuple(map(tuple, new_state)))

        return neighbors

    @staticmethod
    def heuristic(state, goal_state):
        # Manhattan distance heuristic
        distance = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != goal_state[i][j] and state[i][j] != 0:
                    x, y = divmod(goal_state[i][j], 3)
                    distance += abs(x - i) + abs(y - j)
        return distance
