import time

from tkinter import *
from math import sin, cos, pi


root = Tk()

W = root.winfo_screenwidth()
H = root.winfo_screenheight()
print(W, H)
cX, cY = W / 2, H / 2

root.attributes('-fullscreen', True)

c = Canvas(root, width=W, height=H, bg='#000000')
c.pack()

# height = 600
# width = 600
# c = Canvas(root, width=width, height=height, bg="orange")
# c.pack()

ball = c.create_oval(0, 0, 25, 25, fill='red')
line = c.create_line(2, 10, 25, 30)

c.coords(ball)[0] = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
c.coords(ball)[1] = (root.winfo_screenheight() - root.winfo_reqheight()) / 2

# x = cX / 2
# y = cY / 2
# print(x)
# print(y)


def esc(event):
    root.destroy()


def motion():
    # global c
    global x
    global y

    speed = 1
    direction = 5
    direction2 = cos(5)

    coordinates = c.coords(ball)
    x = coordinates[0]
    y = coordinates[1]
    # x = x * sin(pi)
    # y = y * cos(pi)
    print("x: ", x)
    print("y: ", y)

    c.move(ball, 2, 2)

    if c.coords(ball)[2] < W or c.coords(ball)[1] < H:
        time.sleep(0.1)
        root.after(1, motion)
    else:
        exit()


# if __name__ == '__main__':
motion()

root.mainloop()
