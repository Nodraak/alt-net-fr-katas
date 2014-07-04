
from time import sleep

class MazeSolver(object):

    def __init__(self, MazeBuilder):
        self.maze = MazeBuilder()

        self.DIR_UP = 0
        self.DIR_RIGHT = 1
        self.DIR_DOWN = 2
        self.DIR_LEFT = 3

        self.dir = self.DIR_UP
        self.turnWithoutMove = 0

        self.currentPos = (0, 0)
        self.casesDejaVisites = []
        self.casesDejaVisites.append(self.currentPos)

        self.turn = 0

    def solve(self):
        self.maze.draw()
        while not self.maze.am_i_out():
            self.your_turn()
            self.maze.draw()
            print self.turn
            self.turn += 1
            sleep(0.1)

    def your_turn(self):
        maze = self.maze

        if maze.can_i_move():
            frontPos = self.get_front_position()

            if frontPos in self.casesDejaVisites:
                exist = 42
            else:
                exist = None

            if (exist == None) or (self.turnWithoutMove > 3):
                self.currentPos = frontPos
                maze.move()
                if exist == None:
                    self.casesDejaVisites.append(self.currentPos)
                self.turnWithoutMove = 0
            else:
                self.dir = (self.dir + 1) % 4
                maze.turn_right()
                self.turnWithoutMove += 1
        else:
            self.dir = (self.dir + 1) % 4
            maze.turn_right()
            self.turnWithoutMove += 1

    def get_front_position(self):
        if self.dir == 0:
            return (self.currentPos[0] - 1, self.currentPos[1])
        elif self.dir == 1:
            return (self.currentPos[0], self.currentPos[1] + 1)
        elif self.dir == 2:
            return (self.currentPos[0] + 1, self.currentPos[1])
        else:
            return (self.currentPos[0], self.currentPos[1] - 1)

