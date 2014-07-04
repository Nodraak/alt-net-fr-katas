
from time import sleep

class Maze(object):
    """
        draw : print current board
        am_i_out : not very usefull

        Playing :
            can_i_move
            move : perform move in the current dir

            turn_left
            turn_right

        Building the Maze :
            add_wall_horiz
            add_wall_vert

    """

    def __init__(self, width, height, startX, startY):

        # private
        self._DIR_UP = 0
        self._DIR_RIGHT = 1
        self._DIR_DOWN = 2
        self._DIR_LEFT = 3

        self._wallToCheck = [
            [0, 0],
            [1, 0],
            [0, 1],
            [0, 0],
        ]

        self._moves = [
            [0, -1],
            [1, 0],
            [0, 1],
            [-1, 0],
        ]

        # public
        self.width = width
        self.height = height

        self.posX = startX
        self.posY = startY

        self.dir = self._DIR_RIGHT

        self.hWalls = []
        self.vWalls = []

        # init
        for j in range(height+2):
            tmp = []
            for i in range(width+1):
                tmp.append(False)
            self.hWalls.append(tmp)

        for j in range(height+1):
            tmp = []
            for i in range(width+2):
                tmp.append(False)
            self.vWalls.append(tmp)

    def get_char_or_space(self, cond, char):
        if cond:
            return char
        else:
            return ' '

    def draw(self, turn):
        # for each line
        for j in range(self.height+1):
            # init
            seps = '+'
            cells = ''
            # for each col
            for i in range(self.width+1):
                # horiz line of sep
                if i is not self.width:
                    seps += self.get_char_or_space(self.hWalls[j][i], '-') + '+'
                # horiz line of cells (with vert sep)
                cells += self.get_char_or_space(self.vWalls[j][i], '|')
                cells += self.get_char_or_space(self.posY == j and self.posX == i, 'X')
            # print
            print seps
            if j is not self.height:
                print cells
        print turn
        print ''

    def can_i_move(self):
        w2c = self._wallToCheck[self.dir]
        x = self.posX + w2c[0]
        y = self.posY + w2c[1]

        if (self.dir == self._DIR_UP) or (self.dir == self._DIR_DOWN):
            return not (self.hWalls[y][x])
        else:
            return not (self.vWalls[y][x])

    def am_i_out(self):
        return (self.posX < 0) or (self.posX > self.width-1) or (self.posY < 0) or (self.posY > self.height-1)

    def add_wall_horiz(self, x, y):
        if (x < 0) or (x > self.width) or (y < 0) or (y > self.height):
            print 'MAIS T4ES MALADE !!! -> add_wall_horiz()'
        else:
            self.hWalls[y][x] = True;

    def add_wall_vert(self, x, y):
        if (x < 0) or (x > self.width) or (y < 0) or (y > self.height):
            print 'MAIS T4ES MALADE !!! -> add_wall_vert()'
        else:
            self.vWalls[y][x] = True;

    def turn_left(self):
        self.dir = self._DIR_LEFT if (self.dir == self._DIR_UP) else (self.dir - 1)

    def turn_right(self):
        self.dir = self._DIR_UP if (self.dir == self._DIR_LEFT) else (self.dir + 1)

    def move(self):
        if not self.can_i_move():
            return

        move = self._moves[self.dir]
        self.posX += move[0]
        self.posY += move[1]

        if self.am_i_out():
            print 'Gagné !!'


class MazeSolver(object):

    def __init__(self, MazeBuilder):
        self.maze = MazeBuilder()
        self.turn = 0

    def solve(self):
        self.maze.draw(self.turn)
        while not self.maze.am_i_out():
            self.your_turn()
            self.maze.draw(self.turn)

            self.turn += 1
            sleep(0.1)

    def your_turn(self):
        print 'Implement this function (crete your class inheriting from class MazeSolver)'
