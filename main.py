from tkinter import *
import settings
# Overriding the settings of window
root = Tk()
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title(settings.title)
root.resizable(False, False)

#Frames
top_frame = Frame(
    root,
    bg='red',
    width=1000,
    height=100
)

left_frame = Frame(
    root,
    bg='blue',
    width=300,
    height=420
)
top_frame.place(x=0, y=0)
left_frame.place(x=0, y=100)


# Run the window
root.mainloop()
