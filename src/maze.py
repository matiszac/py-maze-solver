import time
import random
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
        win = None,
        seed = None,
    ):
        self._x1, self._y1 = x1, y1
        self._num_rows, self._num_cols = num_rows, num_cols
        self._cell_size_x, self._cell_size_y = cell_size_x, cell_size_y
        self._cells = []
        self._win = win
        if seed is not None:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

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

    def _break_entrance_and_exit(self):
        end_col = len(self._cells) - 1
        end_row = len(self._cells[end_col]) - 1
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0 ,0)
        self._cells[end_col][end_row].has_bottom_wall = False
        self._draw_cell(end_col, end_row)

    def _break_walls_r(self, x, y):
        max_x = len(self._cells) - 1
        max_y = len(self._cells[0]) - 1
        self._cells[x][y]._visited = True
        while True:
            choices = []
            up = (x, y - 1) if y - 1 >= 0 else None
            down = (x, y + 1) if y + 1 <= max_y else None
            left = (x - 1, y) if x - 1 >= 0 else None
            right = (x + 1, y) if x + 1 <= max_x else None
            if up is not None:
                if self._cells[up[0]][up[1]]._visited == False:
                    choices.append('up')
            if down is not None:
                if self._cells[down[0]][down[1]]._visited == False:
                    choices.append('down')
            if left is not None:
                if self._cells[left[0]][left[1]]._visited == False:
                    choices.append('left')
            if right is not None:
                if self._cells[right[0]][right[1]]._visited == False:
                    choices.append('right')
            if len(choices) == 0:
                self._draw_cell(x, y)
                return
            direction = random.choice(choices)
            match direction:
                case 'up':
                    self._cells[x][y].has_top_wall = False
                    self._draw_cell(x, y)
                    self._cells[up[0]][up[1]].has_bottom_wall = False
                    self._draw_cell(up[0], up[1])
                    self._break_walls_r(up[0], up[1])
                case 'down':
                    self._cells[x][y].has_bottom_wall = False
                    self._draw_cell(x, y)
                    self._cells[down[0]][down[1]].has_top_wall = False
                    self._draw_cell(down[0], down[1])
                    self._break_walls_r(down[0], down[1])
                case 'left':
                    self._cells[x][y].has_left_wall = False
                    self._draw_cell(x, y)
                    self._cells[left[0]][left[1]].has_right_wall = False
                    self._draw_cell(left[0], left[1])
                    self._break_walls_r(left[0], left[1])
                case 'right':
                    self._cells[x][y].has_right_wall = False
                    self._draw_cell(x, y)
                    self._cells[right[0]][right[1]].has_left_wall = False
                    self._draw_cell(right[0], right[1])
                    self._break_walls_r(right[0], right[1])

    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, x, y):
        max_x = len(self._cells) - 1
        max_y = len(self._cells[0]) - 1
        curr_cell = self._cells[x][y]
        self._animate()
        curr_cell._visited = True
        if x == max_x and y == max_y:
            return True
        up = (x, y - 1) if y - 1 >= 0 else None
        down = (x, y + 1) if y + 1 <= max_y else None
        left = (x - 1, y) if x - 1 >= 0 else None
        right = (x + 1, y) if x + 1 <= max_x else None
        if up is not None:
            if curr_cell.has_top_wall == False:
                to_cell = self._cells[up[0]][up[1]]
                if to_cell._visited == False:
                    curr_cell.draw_move(to_cell)
                    was_solved = self._solve_r(up[0], up[1])
                    if was_solved:
                        return True
                    curr_cell.draw_move(to_cell, undo = True)
        if down is not None:
            if curr_cell.has_bottom_wall == False:
                to_cell = self._cells[down[0]][down[1]]
                if to_cell._visited == False:
                    curr_cell.draw_move(to_cell)
                    was_solved = self._solve_r(down[0], down[1])
                    if was_solved:
                        return True
                    curr_cell.draw_move(to_cell, undo = True)
        if left is not None:
            if curr_cell.has_left_wall == False:
                to_cell = self._cells[left[0]][left[1]]
                if to_cell._visited == False:
                    curr_cell.draw_move(to_cell)
                    was_solved = self._solve_r(left[0], left[1])
                    if was_solved:
                        return True
                    curr_cell.draw_move(to_cell, undo = True)
        if right is not None:
            if curr_cell.has_right_wall == False:
                to_cell = self._cells[right[0]][right[1]]
                if to_cell._visited == False:
                    curr_cell.draw_move(to_cell)
                    was_solved = self._solve_r(right[0], right[1])
                    if was_solved:
                        return True
                    curr_cell.draw_move(to_cell, undo = True)
        return False

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell._visited = False
        
    def _draw_cell(self, x, y):
        if self._win is None:
            return
        self._cells[x][y].draw()
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.001)
    
