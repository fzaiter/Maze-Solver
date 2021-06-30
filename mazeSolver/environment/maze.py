import os

import numpy as np
from PIL import Image


class Maze:

    def __init__(self, image_path):
        # Get filename without extension
        self.name = os.path.splitext(os.path.basename(image_path))[0]

        self.maze_image = Image.open(image_path)
        self.maze_array = np.asarray(self.maze_image)

        # Since mazes are square we could take one of its dimensions as the size of the maze
        self.size = self.maze_array.shape[0]
        self.start_state, self.finish_state, self.walls, self.empty = self.find_elements()

    def find_elements(self):
        # Find walls, empty and key cells depending on their grey range.
        maze_walls = []
        maze_empty = []
        key_cells = []
        for x in range(self.size):
            for y in range(self.size):
                if self.maze_array[x, y] > 75 and self.maze_array[x, y] < 175:
                    key_cells.append(tuple([x, y]))
                elif self.maze_array[x, y] < 75:
                    maze_walls.append(tuple([x, y]))
                else:
                    maze_empty.append(tuple([x, y]))

        return *key_cells, maze_walls, maze_empty
