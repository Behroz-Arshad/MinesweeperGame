from tkinter import *
import settings
import utils
from cell import Cell

# Overriding the settings of window
root = Tk()
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


c1 = Cell()
c1.create_btn_object(center_frame)
c1.cell_btn_obj.place(x=0, y=0)

# Run the window
root.mainloop()
