from tkinter import *
from math import sin, cos

root = Tk()

W = root.winfo_screenwidth()
H = root.winfo_screenheight()
cX, cY = W / 2, H / 2

root.attributes('-fullscreen', True)

c = Canvas(root, width=W, height=H, bg='#000000')
c.pack()


def esc(event):
    root.destroy()


ball = c.create_oval(0, 100, 40, 140, fill='red')
x = 0
y = 0


def motion():
    global c
    global x
    global y

    c.move(ball, 1, sin(-5))
    coordinates = c.coords(ball)

    x = coordinates[0]
    y = coordinates[1]

    if c.coords(ball)[2] < cX:
        root.after(10, motion())


root.bind('<Escape>', esc)


# def drawEarth():
#     EarthPhoto = PhotoImage(file='Earth2.gif')
#     Earth = Label(root, image=EarthPhoto, borderwidth=0)
#     EarthXs = []
#     EarthYs = []
#     e = 0
#
#     for i in range(420):
#         EarthX = cX + round(200 * sin(e))
#         EarthY = cY - round(200 * cos(e))
#         EarthXs.append(EarthX)
#         EarthYs.append(EarthY)
#         e += 0.015
#     a = 0
#     Earth.place(x=EarthXs[a], y=EarthYs[a])
#     for i in range(420):
#         dx = int(EarthXs[a] - EarthXs[a - 1])
#         dy = int(EarthYs[a] - EarthYs[a - 1])
#         c.move(Earth, dx, dy)
#         a += 1
#
#     del a


# def main():
motion()
root.mainloop()


# main()
