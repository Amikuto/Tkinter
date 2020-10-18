from tkinter import *
import random


def f1(point):
    x = 0
    y = 0.16 * point[1]
    return x, y
    # return 600 - x, 600 - y


def f2(point):
    x = 0.85 * point[0] + 0.04 * point[1]
    y = -0.04 * point[0] + 0.85 * point[1] + 1.6
    # return 600 - x, 600 - y
    return x, y


def f3(point):
    x = 0.20 * point[0] - 0.26 * point[1]
    y = 0.23 * point[0] + 0.22 * point[1] + 1.6
    # return 600 - x, 600 - y
    return x, y


def f4(point):
    x = -0.15 * point[0] + 0.28 * point[1]
    y = 0.26 * point[0] + 0.24 * point[1] + 0.44
    # return 600 - x, 600 - y
    return x, y


def esc(event):
    root.destroy()


root = Tk()
W = 600  # ширина
H = 400  # высота

c = Canvas(root, width=W, height=H, bg='#000000')
c.pack()


root.bind('<Escape>', esc)  # Закрыть окно при помощи esc


def main():
    point = (0, 0)
    for n in range(800):
        # print(point)
        # print(65*point[0]+200, 37*point[1]+150)
        # c.create_oval(65*point[0]+200, 37*point[1]+150, 65*point[0]+200, 37*point[1]+150, width=1, fill='white')
        c.create_oval(W/2 + (55*point[0]), H - (35*point[1]), W/2 + (55*point[0]), H - (35*point[1]),
                      width=0, fill='white')
        rand = random.random()
        if rand < 0.01:
            point = f1(point)
        elif rand < 0.86:
            point = f2(point)
        elif rand < 0.93:
            point = f3(point)
        else:
            point = f4(point)
    root.after(1, main)


if __name__ == "__main__":
    main()
    root.mainloop()
