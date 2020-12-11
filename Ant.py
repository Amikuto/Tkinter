from tkinter import *


def esc(event):
    root.destroy()


root = Tk()

W = 1000
H = 600

c = Canvas(root, width=W, height=H, bg='#000000')
c.pack()

x_start, y_start = W/2, H/2

# c.create_line(x_start, y_start, x_start, y_start, fill="white")

coord = x_start, y_start

coords_list = [coord]

c.create_oval(coord, coord, fill="white", width=1)

if coord in coords_list:
    new_coord =

root.bind('<Escape>', esc)  # Закрыть окно при помощи esc

root.mainloop()
