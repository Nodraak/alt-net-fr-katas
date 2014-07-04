
from time import sleep

class MazeSolver(object):

    def __init__(self, MazeBuilder):
        self.maze = MazeBuilder()

    def solve(self):
        self.maze.draw()
        while not self.maze.am_i_out():
            self.your_turn()
            self.maze.draw()
            sleep(1)

    def your_turn(self):
        maze = self.maze

        maze.turn_left()

        if maze.can_i_move():
            maze.move()
        else:
            maze.turn_right()

            if maze.can_i_move():
                maze.move()
            else:
                maze.turn_right()

