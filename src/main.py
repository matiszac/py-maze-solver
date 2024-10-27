from window import Window
from const import Color
from cell import Cell

CELL_SIZE = 50
WINDOW_WIDTH = 802
WINDOW_HEIGHT = 602
X_CELLS = int(WINDOW_WIDTH // CELL_SIZE)
Y_CELLS = int(WINDOW_HEIGHT // CELL_SIZE)

def main():
    win = Window(WINDOW_WIDTH, WINDOW_HEIGHT)
    cells = generate_cells_from_points(win, generate_cell_points(X_CELLS, Y_CELLS, CELL_SIZE))
    draw_all_cells(cells)
    cells[0].draw_move(cells[Y_CELLS*3])
    win.wait_for_close()


def draw_all_cells(cell_list):
    for cell in cell_list:
        cell.draw(Color.BLACK)

def generate_cell_points(x_cells, y_cells, cell_size, offset=4):
    points = []
    cell_points = []
    for x in range(0, x_cells+1):
        col = []
        for y in range(0, y_cells+1):
            col.append(((x * cell_size)+offset, (y * cell_size)+offset))
        points.append(col)
    for i in range(len(points)-1):
        for p in range(len(points[i])-1):
            cell_points.append((points[i][p], points[i+1][p+1]))
    return cell_points

def generate_cells_from_points(win, cell_points):
    cells = []
    for points in cell_points:
        cells.append(Cell(win, points[0][0], points[0][1], points[1][0], points[1][1]))
    return cells



if __name__ == '__main__':
    main()