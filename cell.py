from tkinter import Button
import random
import settings

class Cell:
    all_elements_list = []
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_obj = None
        self.x = x
        self.y = y
        Cell.all_elements_list.append(self)

    def __repr__(self):
        return f'Cell({self.x},{self.y})'

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            
        )
        btn.bind('<Button-1>', self.left_click_event)
        btn.bind('<Button-3>', self.right_click_event)
        self.cell_btn_obj = btn

    def left_click_event(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()

    def show_mine(self):
        self.cell_btn_obj.configure(bg='red')

    def get_cell_by_axis(self,x,y):
        for cell in Cell.all_elements_list:
            if cell.x == x and cell.y==y:
                return cell
    def show_cell(self):
        self.cell_btn_obj.configure(text=self.surrounded_cells_mines_length)
        print(self.surrounded_cells_mines_length)

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1),
        ]
        cells = [cell for cell in cells if cell]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter
    def right_click_event(self, event):
        print(event)
        print('right click button is pressed')

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all_elements_list, settings.MINE_COUNT)
        for cells in picked_cells:
            cells.is_mine = True

