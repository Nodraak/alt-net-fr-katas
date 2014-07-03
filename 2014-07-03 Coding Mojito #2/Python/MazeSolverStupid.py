
from MazeBuilderSimple import MazeBuilder


maze = MazeBuilder()

while not maze.am_i_out():
    maze.draw()

    maze.turn_right()

    if maze.can_i_move():
        maze.move()
    else:
        maze.turn_left()

    maze.draw()

    if maze.can_i_move():
        maze.move();
    else:
        maze.turn_left()

