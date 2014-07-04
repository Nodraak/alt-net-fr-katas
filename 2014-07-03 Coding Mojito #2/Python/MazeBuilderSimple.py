
from MazeCore import Maze


class MazeBuilder(Maze):

    """
        +-+-+-+
        |X  | |
        + +-+ +
        |     |
        +-+ +-+
        |     |
        +-+-+ +
    """

    def __init__(self):
        Maze.__init__(self, 3, 3, 0, 0)

        self.add_wall_horiz(0, 0);
        self.add_wall_horiz(1, 0);
        self.add_wall_horiz(2, 0);
        self.add_wall_horiz(1, 1);
        self.add_wall_horiz(0, 2);
        self.add_wall_horiz(2, 2);
        self.add_wall_horiz(0, 3);
        self.add_wall_horiz(1, 3);

        self.add_wall_vert(0, 0);
        self.add_wall_vert(2, 0);
        self.add_wall_vert(3, 0);
        self.add_wall_vert(0, 1);
        self.add_wall_vert(3, 1);
        self.add_wall_vert(0, 2);
        self.add_wall_vert(3, 2);

