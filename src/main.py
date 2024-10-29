from window import Window
from maze import Maze

CELL_SIZE = 50
WINDOW_WIDTH = 802
WINDOW_HEIGHT = 602
X_CELLS = int(WINDOW_WIDTH // CELL_SIZE)
Y_CELLS = int(WINDOW_HEIGHT // CELL_SIZE)

def main():
    win = Window(WINDOW_WIDTH, WINDOW_HEIGHT)
    maze = Maze(4, 4, Y_CELLS, X_CELLS, CELL_SIZE, CELL_SIZE, win, 69) # nice
    win.wait_for_close()



if __name__ == '__main__':
    main()