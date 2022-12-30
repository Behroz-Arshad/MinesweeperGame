from tkinter import *
import settings
import utils
from cell import Cell

# Overriding the settings of window
root = Tk()
root.configure(bg='black')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title(settings.title)
root.resizable(False, False)

#Frames
top_frame = Frame(
    root,
    bg='black',
    width=utils.width_percent(100),
    height=utils.height_percent(25)
)

left_frame = Frame(
    root,
    bg='black',
    width=utils.width_percent(25),
    height=utils.height_percent(75)
)

center_frame = Frame(
    root,
    bg='black',
    width=utils.width_percent(75),
    height=utils.height_percent(75)
)


top_frame.place(x=0, y=0)
left_frame.place(x=0, y=utils.height_percent(25))
center_frame.place(x=utils.width_percent(25), y=utils.height_percent(25))

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c1 = Cell(x, y)
        c1.create_btn_object(center_frame)
        c1.cell_btn_obj.grid(column=y, row=x)

Cell.randomize_mines()
for i in Cell.all_elements_list:
    print(i.is_mine)


# c2 = Cell()
# c2.create_btn_object(center_frame)
# c2.cell_btn_obj.grid(column=0, row=1)
# Run the window
root.mainloop()
