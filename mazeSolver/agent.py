from abc import ABC, abstractmethod


class Agent(ABC):

    @abstractmethod
    def __init__(self, name, initial_state, goal_state, colour, maze):
        self.name = name
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.x = initial_state[0]
        self.y = initial_state[1]
        self.colour = colour
        self.maze = maze

        self.previous_state = None
        self.current_state = initial_state

    def choose_action(self, choice):
        # move Right
        if choice == 0:
            self.move(x=1, y=0)
        # move Left
        elif choice == 1:
            self.move(x=-1, y=0)
        # move Down
        elif choice == 2:
            self.move(x=0, y=1)
        # move Up
        elif choice == 3:
            self.move(x=0, y=-1)

    def move(self, x, y):
        self.previous_state = self.current_state

        self.x += x
        self.y += y

        # The following conditions are in case the agent hit the walls of the maze.
        if (self.x, self.y) in self.maze.walls:
            self.x, self.y = self.previous_state

        self.current_state = (self.x, self.y)

    def reset(self):
        self.previous_state = None
        self.current_state = self.initial_state
        self.x = self.initial_state[0]
        self.y = self.initial_state[1]


class Explorer(Agent):

    def __init__(self, name, initial_state, goal_state, colour, maze):
        Agent.__init__(self, name, initial_state, goal_state, colour, maze)


class Solver(Agent):

    def __init__(self, name, initial_state, goal_state, colour, maze, q_table):
        Agent.__init__(self, name, initial_state, goal_state, colour, maze)

        self.q_table = q_table
        self.last_action = None
