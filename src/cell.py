from geometry import Point, Line
from const import Color
from window import Window

class Cell():
    def __init__(self, win: Window, x1, y1, x2, y2):
        self._x1, self._y1 = x1, y1
        self._x2, self._y2 = x2, y2
        self._win = win
        self.has_top_wall = True
        self.has_left_wall = True
        self.has_bottom_wall = True
        self.has_right_wall = True

    def draw_move(self, to_cell, undo=False):
        move_line_color = Color.RED
        if undo:
            move_line_color = Color.GRAY
        fpx, fpy = int((self._x2 - self._x1) / 2 + self._x1), int((self._y2 - self._y1) / 2 + self._y1)
        tpx, tpy = int((to_cell._x2 - to_cell._x1) / 2 + to_cell._x1), int((to_cell._y2 - to_cell._y1) / 2 + to_cell._y1)
        self._win.draw_line(Line(Point(fpx, fpy), Point(tpx, tpy)), move_line_color)
    
    def draw(self, cell_line_color):
        tl, tr = Point(self._x1, self._y1), Point(self._x2, self._y1)
        bl, br = Point(self._x1, self._y2), Point(self._x2, self._y2)
        if self.has_top_wall:
            self._win.draw_line(Line(tr, tl), cell_line_color)
        if self.has_left_wall:
            self._win.draw_line(Line(tl, bl), cell_line_color)
        if self.has_bottom_wall:
            self._win.draw_line(Line(bl, br), cell_line_color)
        if self.has_right_wall:
            self._win.draw_line(Line(br, tr), cell_line_color)