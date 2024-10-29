import unittest
from maze import Maze

CELL_SIZE = 50
WINDOW_WIDTH = 802
WINDOW_HEIGHT = 602
X_CELLS = int(WINDOW_WIDTH // CELL_SIZE)
Y_CELLS = int(WINDOW_HEIGHT // CELL_SIZE)

class TestMaze(unittest.TestCase):
    def test_maze_create_cells(self):
        maze = Maze(0, 0, Y_CELLS, X_CELLS, CELL_SIZE, CELL_SIZE)
        self.assertEqual(
            len(maze._cells),
            X_CELLS,
        )
        self.assertEqual(
            len(maze._cells[0]),
            Y_CELLS,
        )

if __name__ == "__main__":
    unittest.main()