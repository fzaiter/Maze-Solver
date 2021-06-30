import os

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import cv2
from PIL import Image


def setup_results_folder(model_name, maze_name):

    if not os.path.exists("Results"):
        os.makedirs("Results")
    if not os.path.exists(f"Results/{maze_name}"):
        os.makedirs(f"Results/{maze_name}")
    if not os.path.exists(f"Results/{maze_name}/{model_name}"):
        os.makedirs(f"Results/{maze_name}/{model_name}")
    if not os.path.exists(f"Results/{maze_name}/{model_name}/Q-Table"):
        os.makedirs(f"Results/{maze_name}/{model_name}/Q-Table")


def setup_progress_report(model_name, maze_name, eps_initial, episode):

    progress_report = open(f"Results/{maze_name}/{model_name}/Progress Report.txt", "w+")
    progress_report.write(f"Progress Report\n{maze_name} | {model_name}\n\n")
    progress_report.write(f"Episode\t\tEpsilon\t\tMean Cumulative Rewards\tGames Solved\n")
    progress_report.write(f"{episode}\t\t{eps_initial}\t\t-\t\t\t-\n")
    progress_report.close()


def print_report(model_name, maze_name, episode, epsilon, cumulative_rewards, print_progress, games_solved):

    win_rate = round((games_solved/print_progress)*100, 2)
    mean_reward = np.mean(cumulative_rewards[-print_progress:])
    progress_report = open(f"Results/{maze_name}/{model_name}/Progress Report.txt", "a+")
    progress_report.write(f"{episode}\t\t{epsilon}\t\t{mean_reward}\t\t\t{win_rate}%\n")
    progress_report.close()


def append_report_details(model_name, maze_name, first_solved_episode, first_solved_time, training_time):
    progress_report = open(f"Results/{maze_name}/{model_name}/Progress Report.txt", "a+")
    progress_report.write(f"\n* Total training time was {training_time} seconds\n")

    if first_solved_episode != -1:
        progress_report.write(f"\n** First time solved at episode {first_solved_episode} \
                              - Time required: {first_solved_time} seconds\n")
    else:
        progress_report.write("\n** The system never solved the maze\n")
    progress_report.close()


def plot_qtable(model_name, maze, agent, episode):

    if model_name == "Multi Agent - Model":
        if not os.path.exists(f"Results/{maze.name}/{model_name}/Q-Table/{agent.name}"):
            os.makedirs(f"Results/{maze.name}/{model_name}/Q-Table/{agent.name}")

    fig1, ax1 = plt.subplots(1, 1, tight_layout=True)
    fig1.canvas.set_window_title("Q-table")
    ax1.set_title(f"{maze.name} | {model_name} | Episode : {episode}", fontname="Times New Roman",
                  fontsize=10)
    ax1.set_xticks(np.arange(0.5, maze.size, step=1))
    ax1.set_xticklabels([])
    ax1.set_yticks(np.arange(0.5, maze.size, step=1))
    ax1.set_yticklabels([])
    ax1.grid(True)
    ax1.imshow(maze.maze_image, cmap="gray")

    for x in range(maze.size):
        for y in range(maze.size):
            if (y, x) in maze.walls:
                continue
            else:
                action = np.argmax(agent.q_table[y, x])
                dx = 0
                dy = 0
                if action == 0:
                    dy += 0.2
                elif action == 1:
                    dy -= 0.2
                elif action == 2:
                    dx += 0.2
                elif action == 3:
                    dx -= 0.2

                if ((y, x) == maze.start_state) or ((y, x) == maze.finish_state):
                    cell_color = (1, 1, 1)
                else:
                    cell_color = (0.5, 0.5, 0.5)
                ax1.arrow(x, y, dx, dy, color=cell_color, head_width=0.2, head_length=0.1)

    fig1.canvas.draw()

    episode_str = str(episode)
    digits = 4
    while len(episode_str) < digits:
        episode_str = "0" + episode_str

    if model_name == "Multi Agent - Model":
        fig1.savefig(f"Results/{maze.name}/{model_name}/Q-Table/{agent.name}/{model_name}-{agent.name}-{episode_str}",
                     dpi=600)
    else:
        fig1.savefig(f"Results/{maze.name}/{model_name}/Q-Table/{model_name}-{episode_str}",
                     dpi=600)
    plt.close(fig1)


def generate_video(model_name, maze_name, video_name, agent_name=None):
    if model_name == "Multi Agent - Model":
        image_folder = f"Results/{maze_name}/{model_name}/Q-Table/{agent_name}"
    else:
        image_folder = f"Results/{maze_name}/{model_name}/Q-Table"

    images = [img for img in os.listdir(image_folder)]

    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    filename = os.path.join(f"Results/{maze_name}/{model_name}", video_name)

    video = cv2.VideoWriter(filename, fourcc, 1, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    video.release()


def plot_progress(model_name, maze_name, max_steps, print_progress, progress, graph_name):
    fig2, ax2 = plt.subplots(1, 1, tight_layout=True, figsize=(15, 5))
    ax2.set_title(f"{maze_name} | {model_name}", fontname="Times New Roman", fontsize=20,
                  fontweight='bold', pad=20)

    ax2.plot([i for i in range(len(progress))], progress)

    ax2.set_ylabel(f"{graph_name}", fontsize=20)
    ax2.set_xlabel("episode #", fontsize=20)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)

    if graph_name == "Reward":
        ax2.set_ylim([-1000, 1000])
    elif graph_name == "Steps":
        ax2.set_ylim([0, max_steps+1])

    ax2.minorticks_on()
    ax2.tick_params(axis='y', labelsize=18)
    ax2.tick_params(axis='x', labelsize=18)
    ax2.grid(which='major', linewidth='1', linestyle='-')
    ax2.grid(which='minor', linewidth='0.5', linestyle='--')

    fig2.savefig(f"Results/{maze_name}/{model_name}/{model_name} - {graph_name}", dpi=600)
    plt.close(fig2)
