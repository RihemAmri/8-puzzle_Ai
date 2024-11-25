import heapq

class BFSSolver:
    @staticmethod
    def solve_puzzle(initial_state, goal_state):
        
        frontier = []
        heapq.heappush(frontier, (0, initial_state))
        came_from = {initial_state: None}
        iterations = 0

        while frontier:
            _, current_state = heapq.heappop(frontier)
            iterations+=1
            if current_state == goal_state:
                # Reconstruct path
                path = []
                while current_state in came_from:
                    path.insert(0, current_state)
                    current_state = came_from[current_state]
                return path,  iterations

            for next_state in BFSSolver.get_neighbors(current_state):
                if next_state not in came_from:
                    heapq.heappush(frontier, (BFSSolver.heuristic(next_state, goal_state), next_state))
                    came_from[next_state] = current_state
            # print("frontier ",frontier)
            

        return None , iterations

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
