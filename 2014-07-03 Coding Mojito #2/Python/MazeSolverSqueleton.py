
from MazeCore import MazeSolver

class MazeSolverSqueleton(MazeSolver):

    def __init__(self, MazeBuilder):
        MazeSolver.__init__(self, MazeBuilder)
        # other init instructions
        # ...

    def your_turn(self):
        # implement your solver
        if maze.can_i_move():
            maze.move()
        else:
            maze.turn_right()
