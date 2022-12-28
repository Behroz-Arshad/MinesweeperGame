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
        print(event)
        print('left click button is pressed')

    def right_click_event(self, event):
        print(event)
        print('right click button is pressed')

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all_elements_list, settings.MINE_COUNT)
        for cells in picked_cells:
            cells.is_mine = True

