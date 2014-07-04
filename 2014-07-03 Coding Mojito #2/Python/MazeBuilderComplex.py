
from MazeCore import Maze


class MazeBuilder(Maze):

    """
        +-+-+-+-+-+-+-+-+-+
        |                 |
        + + +-+-+-+-+-+-+ +
        |   |             |
        + +-+-+-+ +-+-+-+ +
          |             | |
        +-+ +-+-+-+-+ + +-+
        | |           | | |
        + + + +-+ +-+ + + +
        | | | |     | | | |
        + + + + + + + + + +
        |   |   |X|   |   |
        + + + + +-+ + + + +
        | | | |     | | | |
        + + + +-+ +-+ + + +
        | | |           | |
        + + + +-+-+-+-+ + +
        | |             | |
        + +-+-+-+ +-+-+-+ +
        |                 |
        +-+-+-+-+-+-+-+-+-+
    """

    def __init__(self):
        Maze.__init__(self, 9, 10, 4, 5)

        self.add_wall_horiz(0, 0);

        self.add_wall_horiz(0, 0);
        self.add_wall_horiz(1, 0);
        self.add_wall_horiz(2, 0);
        self.add_wall_horiz(3, 0);
        self.add_wall_horiz(4, 0);
        self.add_wall_horiz(5, 0);
        self.add_wall_horiz(6, 0);
        self.add_wall_horiz(7, 0);
        self.add_wall_horiz(8, 0);

        self.add_wall_horiz(2, 1);
        self.add_wall_horiz(3, 1);
        self.add_wall_horiz(4, 1);
        self.add_wall_horiz(5, 1);
        self.add_wall_horiz(6, 1);
        self.add_wall_horiz(7, 1);

        self.add_wall_horiz(1, 2);
        self.add_wall_horiz(2, 2);
        self.add_wall_horiz(3, 2);

        self.add_wall_horiz(5, 2);
        self.add_wall_horiz(6, 2);
        self.add_wall_horiz(7, 2);

        self.add_wall_horiz(0, 3);

        self.add_wall_horiz(2, 3);
        self.add_wall_horiz(3, 3);
        self.add_wall_horiz(4, 3);
        self.add_wall_horiz(5, 3);

        self.add_wall_horiz(8, 3);

        self.add_wall_horiz(3, 4);
        self.add_wall_horiz(5, 4);

        self.add_wall_horiz(4, 6);

        self.add_wall_horiz(3, 7);
        self.add_wall_horiz(5, 7);

        self.add_wall_horiz(3, 8);
        self.add_wall_horiz(4, 8);
        self.add_wall_horiz(5, 8);
        self.add_wall_horiz(6, 8);

        self.add_wall_horiz(1, 9);
        self.add_wall_horiz(2, 9);
        self.add_wall_horiz(3, 9);

        self.add_wall_horiz(5, 9);
        self.add_wall_horiz(6, 9);
        self.add_wall_horiz(7, 9);

        self.add_wall_horiz(0, 10);
        self.add_wall_horiz(1, 10);
        self.add_wall_horiz(2, 10);
        self.add_wall_horiz(3, 10);
        self.add_wall_horiz(4, 10);
        self.add_wall_horiz(5, 10);
        self.add_wall_horiz(6, 10);
        self.add_wall_horiz(7, 10);
        self.add_wall_horiz(8, 10);

        self.add_wall_vert(0, 0);
        self.add_wall_vert(0, 1);
        self.add_wall_vert(0, 3);
        self.add_wall_vert(0, 4);
        self.add_wall_vert(0, 5);
        self.add_wall_vert(0, 6);
        self.add_wall_vert(0, 7);
        self.add_wall_vert(0, 8);
        self.add_wall_vert(0, 9);

        self.add_wall_vert(1, 2);
        self.add_wall_vert(1, 3);
        self.add_wall_vert(1, 4);

        self.add_wall_vert(1, 6);
        self.add_wall_vert(1, 7);
        self.add_wall_vert(1, 8);

        self.add_wall_vert(2, 1);

        self.add_wall_vert(2, 4);
        self.add_wall_vert(2, 5);
        self.add_wall_vert(2, 6);
        self.add_wall_vert(2, 7);

        self.add_wall_vert(3, 4);
        self.add_wall_vert(3, 6);

        self.add_wall_vert(4, 5);

        self.add_wall_vert(5, 5);

        self.add_wall_vert(6, 4);
        self.add_wall_vert(6, 6);

        self.add_wall_vert(7, 3);
        self.add_wall_vert(7, 4);
        self.add_wall_vert(7, 5);
        self.add_wall_vert(7, 6);

        self.add_wall_vert(8, 2);
        self.add_wall_vert(8, 3);
        self.add_wall_vert(8, 4);

        self.add_wall_vert(8, 6);
        self.add_wall_vert(8, 7);
        self.add_wall_vert(8, 8);

        self.add_wall_vert(9, 0);
        self.add_wall_vert(9, 1);
        self.add_wall_vert(9, 2);
        self.add_wall_vert(9, 3);
        self.add_wall_vert(9, 4);
        self.add_wall_vert(9, 5);
        self.add_wall_vert(9, 6);
        self.add_wall_vert(9, 7);
        self.add_wall_vert(9, 8);
        self.add_wall_vert(9, 9);
