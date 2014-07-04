from MazeCore import Maze


class MazeBuilder(Maze):

    """
        +-+-+-+-+-+-+-+-+
        |X  | |   |   | |
        + +-+ + + + + + +
        |     | |   | |
        +-+ +-+ + + + + +
        |       | | |   |
        +-+-+-+-+-+-+-+-+
    """

    def __init__(self):
        Maze.__init__(self, 8, 3, 0, 0)

        self.add_wall_horiz(0, 0);
        self.add_wall_horiz(1, 0);
        self.add_wall_horiz(2, 0);
        self.add_wall_horiz(3, 0);
        self.add_wall_horiz(4, 0);
        self.add_wall_horiz(5, 0);
        self.add_wall_horiz(6, 0);
        self.add_wall_horiz(7, 0);
        self.add_wall_horiz(1, 1);
        self.add_wall_horiz(0, 2);
        self.add_wall_horiz(2, 2);
        self.add_wall_horiz(0, 3);
        self.add_wall_horiz(1, 3);
        self.add_wall_horiz(2, 3);
        self.add_wall_horiz(3, 3);
        self.add_wall_horiz(4, 3);
        self.add_wall_horiz(5, 3);
        self.add_wall_horiz(6, 3);
        self.add_wall_horiz(7, 3);

        self.add_wall_vert(0, 0);
        self.add_wall_vert(2, 0);
        self.add_wall_vert(3, 0);
        self.add_wall_vert(0, 1);
        self.add_wall_vert(3, 1);
        self.add_wall_vert(0, 2);
        self.add_wall_vert(4, 1);
        self.add_wall_vert(4, 2);
        self.add_wall_vert(5, 0);
        self.add_wall_vert(5, 2);
        self.add_wall_vert(6, 1);
        self.add_wall_vert(6, 2);
        self.add_wall_vert(7, 0);
        self.add_wall_vert(7, 1);
        self.add_wall_vert(8, 0);
        self.add_wall_vert(8, 2);

