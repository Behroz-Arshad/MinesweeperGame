from tkinter import Button


class Cell:
    def __int__(self, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_obj = None


    def create_btn_object(self, location):
        btn = Button(
            location,
            text='C1'
        )
        self.cell_btn_obj = btn
