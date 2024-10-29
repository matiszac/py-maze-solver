import time
from cell import Cell

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self._x1, self._y1 = x1, y1
        self._num_rows, self._num_cols = num_rows, num_cols
        self._cell_size_x, self._cell_size_y = cell_size_x, cell_size_y
        self._cells = []
        self._win = win
        self._create_cells()

    def _create_cells(self):
        for x in range(self._num_cols):
            col = []
            for y in range(self._num_rows):
                x1 = (x * self._cell_size_x)+self._x1
                y1 = (y * self._cell_size_y)+self._y1
                col.append(Cell(self._win, x1, y1, x1 + self._cell_size_x, y1 + self._cell_size_y))
            self._cells.append(col)
        for x in range(self._num_cols):
            for y in range(self._num_rows):
                self._draw_cell(x, y)

    def _draw_cell(self, x, y):
        if self._win is None:
            return
        self._cells[x][y].draw()
        self._animate()
    

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.005)
    
