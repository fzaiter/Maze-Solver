import time
from abc import ABC, abstractmethod

import numpy as np
import cv2
from PIL import Image

import utilities


class Model(ABC):

    @abstractmethod
    def __init__(self, name, maze):
        self.name = name
        self.maze = maze

        self.solution = []
        self.games_solved = 0
        self.first_solved = False
        self.first_solved_episode = -1
        self.first_solved_time = -1
        self.final_episode = False

        self.cumulative_rewards = []
        self.cumulative_steps = []

    @abstractmethod
    def train(self):
        return

    def setup_data_collection(model, epsilon):

        utilities.setup_results_folder(model.name, model.maze.name)
        utilities.setup_progress_report(model.name, model.maze.name, epsilon, episode=0)
        for solver in model.solvers:
            utilities.plot_qtable(model.name, model.maze, solver, episode=0)

    def track_progress(model, episode, episodes, epsilon, print_progress, show_progress, show_solution):

        if episode % print_progress == 0 and episode != 0:
            utilities.print_report(model.name, model.maze.name, episode, epsilon,
                                   model.cumulative_rewards, print_progress, model.games_solved)
            model.games_solved = 0

        if (episode % show_progress == 0) and episode != 0:
            model.show = True

        elif episode == episodes-1:
            model.final_episode = True
            model.show = True

    def track_qtable(model, episode, plot_table):

        if (episode % plot_table == 0) and episode != 0:
            for solver in model.solvers:
                utilities.plot_qtable(model.name, model.maze, solver, episode)

    def set_first_solve(model, episode, start_time):

        model.first_solved_episode = episode
        model.first_solved_time = round(time.perf_counter()-start_time, 4)
        model.first_solved = True

    def show_training_episode(model, episode, episodes, show_solution):

        env = np.zeros((model.maze.size, model.maze.size, 3), dtype=np.uint8)

        for x in range(model.maze.size):
            for y in range(model.maze.size):
                env[x, y] = model.maze.maze_array[x, y]

        if model.final_episode:
            for solver in model.solvers:
                model.solution.append(solver.current_state)
                for state in model.solution:
                    if (state != model.maze.start_state and state != model.maze.finish_state):
                        env[state] = (0, 175, 255)

            env_resized = cv2.resize(env, (1000, 1000), interpolation=cv2.INTER_AREA)
            cv2.imwrite(f"Results/{model.maze.name}/{model.name}/Solution.png",
                        env_resized, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

        else:
            for agent in model.agents:
                env[agent.x][agent.y] = agent.colour

        if episode != episodes-1 or show_solution:
            img = Image.fromarray(env, 'RGB')
            img = img.resize((600, 600), Image.NEAREST)
            cv2.imshow(f"Learning process || {model.name}", np.array(img))

    def generate_results(model, max_steps, print_progress, start_time):

        total_training_time = round(time.perf_counter()-start_time, 4)

        # Append first episode maze was solved and total training time at the end of report
        utilities.append_report_details(model.name, model.maze.name, model.first_solved_episode,
                                        model.first_solved_time, total_training_time)

        learning_progress = np.convolve(model.cumulative_rewards, np.ones((print_progress)) / print_progress,
                                        mode="valid")
        steps_progress = np.convolve(model.cumulative_steps, np.ones((print_progress)) / print_progress,
                                     mode="valid")

        # Generate results
        for solver in model.solvers:
            video_title = "Q-Table_" + solver.name + ".avi"
            utilities.generate_video(model.name, model.maze.name, video_title, solver.name)

        utilities.plot_progress(model.name, model.maze.name, max_steps, print_progress,
                                learning_progress, "Reward")
        utilities.plot_progress(model.name, model.maze.name, max_steps, print_progress,
                                steps_progress, "Steps")
