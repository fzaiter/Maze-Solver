import os

import numpy as np
import cv2
import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox
from PIL import ImageTk, Image

from environment.maze import Maze
import models
import agent

current_directory = os.getcwd()


class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # Create main tkinter window
        self.title('Maze Solver')
        self.geometry("800x500")
        self.resizable(0, 0)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.grid_rowconfigure(0, minsize=20)
        self.grid_rowconfigure(6, minsize=20)
        self.grid_rowconfigure(10, minsize=20)
        self.grid_rowconfigure(14, minsize=20)
        self.grid_rowconfigure(18, minsize=20)
        self.grid_rowconfigure(20, minsize=10)
        self.grid_rowconfigure(22, minsize=10)

        self.grid_columnconfigure(0, pad=20)
        self.grid_columnconfigure(1, pad=10)
        self.grid_columnconfigure(2, pad=10)
        self.grid_columnconfigure(3, pad=10)
        self.grid_columnconfigure(4, pad=10)

        self.episodes = 0
        # Maximum amount of steps the program takes before terminating
        self. max_steps = 200
        # Learning rate and discounted cumulative reward
        self.learning_rate = 0.1
        self.discount = 0.995
        # Greedy exploration: epsilon and epsilon decay
        self.eps_initial = 0.9
        self.eps_decay = 0
        # Rewards
        self.move_penalty = -1
        self.offgrid_penalty = -10
        self.goal_reward = 1000
        # Progress output
        self.show_progress = 500
        self.plot_table = 100
        self.print_progress = 50
        self.show_solution = False
        # White image as placeholder of imported maze design.
        white_array = 255*np.ones((350, 350, 3), dtype=np.uint8)
        maze_img = Image.fromarray(white_array, 'RGB')
        self.maze_tkimg = ImageTk.PhotoImage(image=maze_img)
        self.maze_imported = False

        # 1. PARAMETERS
        self.label_parameters = Label(self, text="PARAMETERS", font='Helvetica 10 bold')
        self.label_parameters.grid(row=1, column=0)

        self.button_update_parameters = Button(self, text="Update", command=self.update_parameters)
        self.button_update_parameters.grid(row=2, column=0, rowspan=4)

        self.label_episodes = Label(self, text="Episodes")
        self.label_episodes.grid(row=2, column=1)
        self.episodes_options = [0, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
        self.clicked_episodes = tk.IntVar()
        self.dropmenu_episodes = OptionMenu(self, self.clicked_episodes, *self.episodes_options)
        self.dropmenu_episodes.grid(row=3, column=1)

        self.label_eps_initial = Label(self, text="Epsilon Initial")
        self.label_eps_initial.grid(row=2, column=2)
        self.label_eps_initial_value = Label(self, text="0.9")
        self.label_eps_initial_value.grid(row=3, column=2)

        self.label_eps_decay = Label(self, text="Epsilon Decay")
        self.label_eps_decay.grid(row=2, column=3)
        self.label_eps_decay_value = Label(self, text=self.eps_decay)
        self.label_eps_decay_value.grid(row=3, column=3)

        self.label_steps = Label(self, text="Max Steps", )
        self.label_steps.grid(row=4, column=1)
        self.text_steps = Entry(self, justify=tk.CENTER, width=10)
        self.text_steps.insert(0, self.max_steps)
        self.text_steps.grid(row=5, column=1)

        self.label_lrate = Label(self, text="Learning Rate")
        self.label_lrate.grid(row=4, column=2)
        self.text_lrate = Entry(self, justify=tk.CENTER, width=10)
        self.text_lrate.insert(0, self.learning_rate)
        self.text_lrate.grid(row=5, column=2)

        self.label_discount = Label(self, text="Discount")
        self.label_discount.grid(row=4, column=3)
        self.text_discount = Entry(self, justify=tk.CENTER, width=10)
        self.text_discount.insert(0, self.discount)
        self.text_discount.grid(row=5, column=3)

        # 2. REWARDS
        self.label_rewards = Label(self, text="REWARDS", font='Helvetica 10 bold')
        self.label_rewards.grid(row=7, column=0)

        self.button_update_rewards = Button(self, text="Update", command=self.update_rewards)
        self.button_update_rewards.grid(row=8, column=0, rowspan=2)

        self.label_goal_reward = Label(self, text="Goal Reward")
        self.label_goal_reward.grid(row=8, column=1)
        self.text_goal_reward = Entry(self, justify=tk.CENTER, width=10)
        self.text_goal_reward.insert(0, self.goal_reward)
        self.text_goal_reward.grid(row=9, column=1)

        self.label_move_penalty = Label(self, text="Move Penalty")
        self.label_move_penalty.grid(row=8, column=2)
        self.text_move_penalty = Entry(self, justify=tk.CENTER, width=10)
        self.text_move_penalty.insert(0, self.move_penalty)
        self.text_move_penalty.grid(row=9, column=2)

        self.label_offgrid_penalty = Label(self, text="Off-grid Penalty")
        self.label_offgrid_penalty.grid(row=8, column=3)
        self.text_offgrid_penalty = Entry(self, justify=tk.CENTER, width=10)
        self.text_offgrid_penalty.insert(0, self.offgrid_penalty)
        self.text_offgrid_penalty.grid(row=9, column=3)

        # 3. RESULTS
        self.label_results = Label(self, text="RESULTS", font='Helvetica 10 bold')
        self.label_results.grid(row=11, column=0)

        self.button_update_results = Button(self, text="Update", command=self.update_results)
        self.button_update_results.grid(row=12, column=0, rowspan=2)

        self.label_show = Label(self, text="Show Progress")
        self.label_show.grid(row=12, column=1)
        self.text_show = Entry(self, justify=tk.CENTER, width=10)
        self.text_show.insert(0, self.show_progress)
        self.text_show.grid(row=13, column=1)

        self.label_plot = Label(self, text="Plot Table")
        self.label_plot.grid(row=12, column=2)
        self.text_plot = Entry(self, justify=tk.CENTER, width=10)
        self.text_plot.insert(0, self.plot_table)
        self.text_plot.grid(row=13, column=2)

        self.label_print = Label(self, text="Print Progress")
        self.label_print.grid(row=12, column=3)
        self.text_print = Entry(self, justify=tk.CENTER, width=10)
        self.text_print.insert(0, self.print_progress)
        self.text_print.grid(row=13, column=3)

        self.clicked_solution = tk.IntVar()
        self.check_solution = tk.Checkbutton(self, text="Show solution in the last episode",
                                             variable=self.clicked_solution, onvalue=1, offvalue=0,
                                             command=self.update_show_solution)
        self.check_solution.grid(row=14, column=1, columnspan=3)

        # 4. MAZE AND MODEL
        self.label_maze_model = Label(self, text="MAZE AND MODEL", font='Helvetica 10 bold')
        self.label_maze_model.grid(row=16, column=0)

        self.maze_designs = os.listdir(os.path.join(current_directory, "environment",
                                                    "Images-Maze"))
        self.maze_designs.insert(0, "-")
        self.model_options = ["-", "Single Agent - Start", "Single Agent - End",
                              "Single and Explorer - Start", "Single and Explorer - End",
                              "Multi Agent"]

        self.label_maze = Label(self, text="Select maze")
        self.label_maze.grid(row=17, column=1)
        self.clicked_maze = tk.StringVar()
        self.dropmenu_maze = OptionMenu(self, self.clicked_maze, *self.maze_designs)
        self.dropmenu_maze.grid(row=17, column=2, columnspan=2)

        self.label_model = Label(self, text="Select model")
        self.label_model.grid(row=18, column=1)
        self.clicked_model = tk.StringVar()
        self.dropmenu_model = OptionMenu(self, self.clicked_model, *self.model_options)
        self.dropmenu_model.grid(row=18, column=2, columnspan=2)

        self.button_train = Button(self, text="Import Maze", command=self.import_maze)
        self.button_train.grid(row=21, column=2)

        self.button_train = Button(self, text="Train", command=self.train)
        self.button_train.grid(row=21, column=3)

        self.label_notes = Label(self, text="",  font='Helvetica 8 italic')
        self.label_notes.grid(row=25, column=0, columnspan=2)

        # 5. MAZE
        self.label_maze = Label(self, text="MAZE", font='Helvetica 10 bold')
        self.label_maze.grid(row=1, column=4)

        self.canvas = tk.Canvas(self, width=350, height=350)
        self.image_container = self.canvas.create_image(0, 0, anchor='nw', image=self.maze_tkimg)
        self.canvas.grid(row=2, column=4, rowspan=17)

        self.label_maze_status = Label(self, text="")
        self.label_maze_status.grid(row=20, column=4)

        self.label_train_status = Label(self, text="",  font='Helvetica 9 italic')
        self.label_train_status.grid(row=23, column=4)

    def associate_decay(self, episodes):
        if episodes == 10:
            self.eps_decay = 0.55
        elif episodes == 20:
            self.eps_decay = 0.75
        elif episodes == 50:
            self.eps_decay = 0.91
        elif episodes == 100:
            self.eps_decay = 0.945
        elif episodes == 200:
            self.eps_decay = 0.968
        elif episodes == 500:
            self.eps_decay = 0.988
        elif episodes == 1000:
            self.eps_decay = 0.994
        elif episodes == 2000:
            self.eps_decay = 0.997
        elif episodes == 5000:
            self.eps_decay = 0.9987

    def on_closing(self):
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()

    def update_parameters(self):
        self.episodes = self.clicked_episodes.get()
        self.associate_decay(self.episodes)
        self.label_eps_decay_value.config(text=self.eps_decay)
        self.max_steps = int(self.text_steps.get())
        self.learning_rate = float(self.text_lrate.get())
        self.discount = float(self.text_discount.get())

        self.label_notes.config(text="Parameters Updated")

    def update_rewards(self):
        self.goal_reward = int(self.text_goal_reward.get())
        self.move_penalty = int(self.text_move_penalty.get())
        self.offgrid_penalty = int(self.text_offgrid_penalty.get())

        self.label_notes.config(text="Rewards Updated")

    def update_results(self):
        self.show_progress = int(self.text_show.get())
        self.plot_table = int(self.text_plot.get())
        self.print_progress = int(self.text_print.get())

        self.label_notes.config(text="Results Updated")

    def update_show_solution(self):
        if self.clicked_solution.get() == 1:
            self.show_solution = True
        else:
            self.show_solution = False

        self.label_notes.config(text="Show solution updated")

    def draw_maze(self):
        env = np.zeros((self.maze.size, self.maze.size, 3), dtype=np.uint8)

        for x in range(self.maze.size):
            for y in range(self.maze.size):
                env[x, y] = self.maze.maze_array[x, y]

        maze_img = Image.fromarray(env, 'RGB')
        maze_resized = maze_img.resize((350, 350), Image.NEAREST)
        self.maze_tkimg = ImageTk.PhotoImage(maze_resized)
        self.canvas.itemconfig(self.image_container, image=self.maze_tkimg)

    def import_maze(self):
        if self.clicked_maze.get() == "-":
            tk.messagebox.showinfo('Error', 'Please select maze and try again')

        else:
            self.maze = Maze(os.path.join(current_directory, "environment",
                                          "Images-Maze", self.clicked_maze.get()))
            self.label_maze_status.config(text=f"Maze imported: {self.maze.name}")
            self.draw_maze()
            self.maze_imported = True

    def show_results(self, maze, model):
        results_path = os.path.join(current_directory, f"Results\\{maze}\\{model}")
        os.startfile(results_path)

    def create_qtable(self, seed):
        np.random.seed(seed)
        q_table = {}
        for x1 in range(-self.maze.size+1, self.maze.size):
            for y1 in range(-self.maze.size+1, self.maze.size):
                q_table[(x1, y1)] = [np.random.uniform(0, 1) for i in range(4)]
        return q_table

    def train(self):

        if self.episodes != 0 and self.maze_imported and self.clicked_model.get() != "-":

            q_table = self.create_qtable(13)

            # Create agents -solvers and explorers- to be used on models.
            solver_start = agent.Solver("Start agent", self.maze.start_state, self.maze.finish_state,
                                        (255, 175, 0), self.maze, q_table)
            solver_finish = agent.Solver("Finish agent", self.maze.finish_state, self.maze.start_state,
                                         (0, 255, 0), self.maze, q_table)
            explorer_start = agent.Explorer("Start explorer", self.maze.start_state, self.maze.finish_state,
                                            (255, 175, 175), self.maze)
            explorer_finish = agent.Explorer("Finish explorer", self.maze.finish_state, self.maze.start_state,
                                             (0, 175, 175), self.maze)

            train_rewards = [self.move_penalty, self.offgrid_penalty, self.goal_reward]

            selected_model = self.clicked_model.get()
            self.label_train_status.config(text=f"Running training for {selected_model}")

            if selected_model == "Single Agent - Start":
                model = models.SingleModel("Single Agent - Start Model", self.maze, solver_start)
            elif selected_model == "Single Agent - End":
                model = models.SingleModel("Single Agent - Finish Model", self.maze, solver_finish)
            elif selected_model == "Single and Explorer - Start":
                model = models.ExplorerModel("Explorer Agent - Start Model", self.maze,
                                             solver_start, explorer_start)
            elif selected_model == "Single and Explorer - End":
                model = models.ExplorerModel("Explorer Agent - Finish Model", self.maze,
                                             solver_finish, explorer_finish)
            elif selected_model == "Multi Agent":
                model = models.MultiModel("Multi Agent - Model", self.maze,
                                          solver_start, solver_finish)
            else:
                tk.messagebox.showinfo('Error', 'Please select model and try again')

            model.train(self.episodes, self.max_steps, self.learning_rate, self.discount,
                        self.eps_initial, self.eps_decay, train_rewards,
                        self.show_progress, self.plot_table, self.print_progress, self.show_solution)

            self.label_train_status.config(text=f"Training finished")
            self.show_results(self.maze.name, model.name)

        else:
            if self.episodes == 0:
                tk.messagebox.showinfo('Error - No episodes', 'Please select episodes and update.')
            elif not self.maze_imported:
                tk.messagebox.showinfo('Error - No maze', 'Please select maze and import.')
            elif self.clicked_model.get() == "-":
                tk.messagebox.showinfo('Error - No model', 'Please select model for training.')


if __name__ == '__main__':
    app = Application()

    app.mainloop()
