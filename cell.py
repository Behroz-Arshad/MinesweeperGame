from tkinter import Button, Label, messagebox
import random
import settings
import sys


class Cell:
    all_elements_list = []
    cell_count_label_obj = None
    cell_count = settings.CELL_COUNT

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_obj = None
        self.is_opened = False
        self.is_mined_candidate = False
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

    @staticmethod
    def create_label_object(location):
        lbl = Label(
            location,
            text=f'Cell Left:{Cell.cell_count}',
            bg='black',
            fg='white',
            font=("", 30)
        )
        Cell.cell_count_label_obj = lbl

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
        messagebox.showwarning('Game Over', 'You have clicked the mine')
        sys.exit()

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all_elements_list:
            if cell.x == x and cell.y == y:
                return cell

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_obj.configure(text=self.surrounded_cells_mines_length)
            if Cell.cell_count_label_obj:
                Cell.cell_count_label_obj.configure(text=f'Cell Left:{Cell.cell_count}')

        self.is_opened = True

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
        if not self.is_mined_candidate:
            self.cell_btn_obj.configure(bg='orange')
            self.is_mined_candidate = True
        else:
            self.cell_btn_obj.configure(bg='#F0F0F0')
            self.is_mined_candidate = False

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all_elements_list, settings.MINE_COUNT)
        for cells in picked_cells:
            cells.is_mine = True
