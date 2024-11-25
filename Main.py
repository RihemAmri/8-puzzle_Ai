import tkinter as tk
import random
from tkinter import messagebox
from a_star import AStarSolver
from hill_climbing import HillClimbingSolver
from collections import deque
from BFS import BFSSolver
class EightPuzzle:
    def __init__(self, master):
        self.master = master
        self.master.title("8-Puzzle Game")
        self.master.geometry("290x405")
        self.tiles = [[None for _ in range(3)] for _ in range(3)]
        self.empty_tile = (2, 2)
        self.initialize_puzzle()
        self.create_buttons()
        self.master.config(bg="#FFB6C1")

    def initialize_puzzle(self):
        numbers = list(range(1, 9)) + [0]
        random.shuffle(numbers)
        idx = 0
        for i in range(3):
            for j in range(3):
                number = numbers[idx]
                idx += 1
                self.tiles[i][j] = number
                if number == 0:
                    self.empty_tile = (i, j)


    def create_buttons(self):
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                if self.tiles[i][j] != 0:
                    btn = tk.Button(self.master, text=str(self.tiles[i][j]), font=('Arial', 24), width=4, height=2)
                    btn.grid(row=i, column=j, padx=5, pady=5)
                    self.buttons[i][j] = btn
                else:
                    self.buttons[i][j] = None
        reset_button = tk.Button(self.master, text="Reset", width=9, height=1, font=('Arial', 10), command=self.reset)
        reset_button.grid(row=3, column=1, padx=5, pady=5)

        a_star_button = tk.Button(self.master, text="A*", width=9, height=1, font=('Arial', 10), command=self.run_a_star)
        a_star_button.grid(row=4, column=0, padx=5, pady=5)

        hill_climbing_button = tk.Button(self.master, text="Hill Climbing", font=('Arial', 10), width=9, height=1, command=self.run_hill_climbing)
        hill_climbing_button.grid(row=4, column=1, padx=5, pady=5)

        bfs_button = tk.Button(self.master, text="BFS", width=9, height=1, font=('Arial', 10), command=self.run_bfs)
        bfs_button.grid(row=4, column=2, padx=5, pady=5)

    def move_tile(self, i, j):
        ei, ej = self.empty_tile
        if (abs(i - ei) == 1 and j == ej) or (abs(j - ej) == 1 and i == ej):
            self.tiles[ei][ej], self.tiles[i][j] = self.tiles[i][j], self.tiles[ei][ej]
            self.buttons[ei][ej], self.buttons[i][j] = self.buttons[i][j], self.buttons[ei][ej]
            if self.buttons[ei][ej]:
                self.buttons[ei][ej].grid(row=ei, column=ej)
            if self.buttons[i][j]:
                self.buttons[i][j].grid(row=i, column=j)
            self.empty_tile = (i, j)
            

    # def check_victory(self):
    #     correct = list(range(1, 9)) + [0]
    #     current = [self.tiles[i][j] for i in range(3) for j in range(3)]
    #     if current == correct:
    #         self.show_victory_message()

    # def show_victory_message(self):
    #     victory_window = tk.Toplevel(self.master)
    #     victory_window.title("Victory")
    #     tk.Label(victory_window, text="Congratulations! You solved the puzzle!", font=('Arial', 16)).pack(padx=20, pady=20)
    #     tk.Button(victory_window, text="OK", command=victory_window.destroy).pack(pady=10)

    def reset(self):
        print("Let's Do it Again !!")
        self.shuffle()

    def shuffle(self):
        # for _ in range(100):
        #     i, j = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        #     new_i, new_j = self.empty_tile[0] + i, self.empty_tile[1] + j
        #     if 0 <= new_i < 3 and 0 <= new_j < 3:
        #         self.move_tile(new_i, new_j)
        self.initialize_puzzle()
        print("chakchouka : ",self.tiles)
        self.update_ui_with_state(self.tiles)
        

    def update_ui_with_state(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    if self.buttons[i][j]:
                        self.buttons[i][j].grid_forget()
                        self.buttons[i][j] = None
                else:
                    if self.buttons[i][j]:
                        self.buttons[i][j].config(text=str(state[i][j]))
                    else:
                        btn = tk.Button(self.master, text=str(state[i][j]), font=('Arial', 24), width=4, height=2)
                        btn.grid(row=i, column=j, padx=5, pady=5)
                        self.buttons[i][j] = btn

    def animate_solution(self, solution):
        if solution:
            def step(index):
                if index < len(solution):
                    self.update_ui_with_state(solution[index])
                    self.master.after(1000, step, index + 1)  # Update every 1000 ms
            step(0)
        else:
            messagebox.showinfo("Result", "No solution found.")

    def run_a_star(self):
        print("A Star")
        initial_state = tuple(map(tuple, self.tiles))
        print("Etat initial:")
        for s in initial_state:
            print(s)
        print("-------------")
        goal_state = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
        print("Etat final:")
        for s in goal_state:
            print(s)
        print("-------------")
        solution, iterations = AStarSolver.solve_puzzle(initial_state, goal_state)
        self.animate_solution(solution)
        if solution:
            print("Solution found:")
            i = 0
            for step in solution:
                i += 1
                print("Step:", i)
                for s in step:
                    print(s)
                print("-------------")
            print("resolved in ", i, " step")    
            print("Resolved in ", iterations, " iterations")
        else:
            print("No solution found.")


    def run_hill_climbing(self):
        print("Hill Climbing")
        initial_state = tuple(map(tuple, self.tiles))
        print(initial_state)
        goal_state = ((0, 1, 2), (3, 4, 5), (6, 7, 8))
        print(goal_state)
        
        # Appel de la fonction solve_puzzle et décomposition du tuple retourné
        solution, iterations = HillClimbingSolver.solve_puzzle(initial_state, goal_state)
        
        if solution:
            print("Solution found:")
            self.animate_solution(solution)
            for i, step in enumerate(solution, start=1):
                print(f"Step {i}:")
                for row in step:
                    print(row)
            print(f"Resolved in {iterations} steps")
        else:
            print("No solution found.")


    def run_bfs(self):
        print("BFS")
        initial_state = tuple(map(tuple, self.tiles))
        print("Etat initial:")
        for s in initial_state:
            print(s)
        print("-------------")
        goal_state = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
        print("Etat final:")
        for s in goal_state:
            print(s)
        print("-------------")
        solution, iterations = BFSSolver.solve_puzzle(initial_state, goal_state)
        self.animate_solution(solution)
        if solution:
            print("Solution found:")
            i = 0
            for step in solution:
                i += 1
                print("Step:", i)
                for s in step:
                    print(s)
                print("-------------")
            print("resolved in ", i, " step")
            print("Resolved in ", iterations, " iterations")
        else:
            print("No solution found.")



if __name__ == "__main__":
    root = tk.Tk()
    game = EightPuzzle(root)
    root.mainloop()


