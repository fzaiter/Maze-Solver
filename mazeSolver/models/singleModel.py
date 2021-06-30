import time

import numpy as np
import cv2

from models.model import Model


class SingleModel(Model):

    def __init__(self, name, maze, solver):
        Model.__init__(self, name, maze)

        self.solver = solver
        self.agents = [self.solver]
        self.solvers = [self.solver]

    def train(self, episodes, max_steps, learning_rate, discount, eps_initial, eps_decay,
              train_rewards, show_progress, plot_table, print_progress, show_solution):

        epsilon = eps_initial

        self.setup_data_collection(epsilon)

        # Rewards
        move_penalty = train_rewards[0]
        offgrid_penalty = train_rewards[1]
        goal_reward = train_rewards[2]

        start_time = time.perf_counter()

        for episode in range(episodes):
            episode_reward = 0
            episode_steps = 0

            # The following variable will confirm that a correct solution has been found
            solved = False

            # Track results of learning process
            self.show = False
            self.track_progress(episode, episodes, epsilon, print_progress, show_progress, show_solution)

            # Relocate agent in initial position
            self.solver.reset()

            # Episode will terminate after a series of steps to stop agents wandering around.
            for step in range(max_steps):

                episode_steps += 1

                # 1. Decide next action (exploration vs exploitation) and move.
                if np.random.random() > epsilon:
                    action = np.argmax(self.solver.q_table[self.solver.current_state])
                else:
                    action = np.random.randint(0, 4)

                self.solver.choose_action(action)

                # 2. Find reward or penalty for that action.
                if self.solver.current_state == self.solver.goal_state:
                    reward = goal_reward
                    solved = True
                    self.games_solved += 1
                    if self.first_solved is False:
                        self.set_first_solve(episode, start_time)

                # If the state is the same it means that it tried and illegal movement.
                elif self.solver.current_state == self.solver.previous_state:
                    reward = offgrid_penalty
                else:
                    reward = move_penalty

                # 3. Update q-table
                max_future_q = np.max(self.solver.q_table[self.solver.current_state])
                current_q = self.solver.q_table[self.solver.previous_state][action]

                if reward == goal_reward:
                    new_q = goal_reward
                else:
                    new_q = current_q + (learning_rate * (reward + (discount * max_future_q) - current_q))

                self.solver.q_table[self.solver.previous_state][action] = new_q

                # 4. Plot progress for analysis.
                episode_reward += reward

                if self.show:
                    self.show_training_episode(episode, episodes, show_solution)

                    # Pause image if player gets to goal or if we are in the final episode
                    if reward == (goal_reward):
                        if cv2.waitKey(0) & 0xFF == ord('q'):
                            break
                    else:
                        if cv2.waitKey(100) & 0xFF == ord('q'):
                            break

                if solved:
                    break

            self.cumulative_rewards.append(episode_reward)
            self.cumulative_steps.append(episode_steps)

            # Epsilon value is rounded to avoid having really long values.
            epsilon = round(epsilon*eps_decay, 5)

            self.track_qtable(episode, plot_table)

        self.generate_results(max_steps, print_progress, start_time)
