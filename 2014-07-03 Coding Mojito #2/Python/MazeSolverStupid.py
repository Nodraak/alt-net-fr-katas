
from MazeCore import MazeSolver

class MazeSolverStupid(MazeSolver):

    def __init__(self, MazeBuilder):
        MazeSolver.__init__(self, MazeBuilder)

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

