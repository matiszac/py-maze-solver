from tkinter import Tk, BOTH, Canvas
from geometry import Line
from const import Color

class Window():
    def __init__(self, width, height, bg=Color.WHITE):
        self.__root = Tk()
        self.__root.title('Maze Solver')
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.__root, background = bg, width = width, height = height)
        self.canvas.pack()
        self.running = False
    
    def draw_line(self, line: Line, color=Color.BLACK):
        line.draw(self.canvas, color)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running  = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False