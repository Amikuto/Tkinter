from tkinter import *
import random


def f1(point):
    x = 0
    y = 0.16 * point[1]
    return x, y


def f2(point):
    x = 0.85 * point[0] + 0.04 * point[1]
    y = -0.04 * point[0] + 0.85 * point[1] + 1.6
    return x, y


def f3(point):
    x = 0.20 * point[0] - 0.26 * point[1]
    y = 0.23 * point[0] + 0.22 * point[1] + 1.6
    return x, y


def f4(point):
    x = -0.15 * point[0] + 0.28 * point[1]
    y = 0.26 * point[0] + 0.24 * point[1] + 0.44
    return x, y


def esc(event):
    root.destroy()


def main():
    point = (0, 0)
    for n in range(800):
        rand = random.random()

        if rand < 0.01:
            point = f1(point)  # Отрисовка стебля
        elif rand < 0.86:
            point = f2(point)  # Отрисовка меньших листьев
        elif rand < 0.93:
            point = f3(point)  # Отрисовка левой части
        else:
            point = f4(point)  # Отрисовка правой части

        draw_point = W/2 + (leaf_w * point[0]), H - (leaf_h * point[1])
        c.create_oval(draw_point, draw_point, width=0, fill='white')

    root.after(1, main)


# class Image:
#     def __init__(self, master, leaf_w, leaf_h, start_point, rep_num):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.leaf_w = leaf_w
#         self.leaf_h = leaf_h
#         self.point = start_point
#         self.rep_num = rep_num
#
    # def run(self):
    #     self.point = (0, 0)
    #     for n in range(self.rep_num):
    #         rand = random.random()
    #
    #         if rand < 0.01:
    #             self.point = f1(self.point)  # Отрисовка стебля
    #         elif rand < 0.86:
    #             self.point = f2(self.point)  # Отрисовка меньших листьев
    #         elif rand < 0.93:
    #             self.point = f3(self.point)  # Отрисовка левой части
    #         else:
    #             self.point = f4(self.point)  # Отрисовка правой части
    #
    #         draw_point = W / 2 + (self.leaf_w * self.point[0]), H - (self.leaf_h * self.point[1])
    #         c.create_oval(draw_point, draw_point, width=0, fill='white')
    #
    #     root.after(1, self.run())


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.c = Canvas(root, width=W, height=H, bg='#000000')
        self.c.pack()
        # self.rep_num = rep_num

    def run(self, leaf_w, leaf_h):
        self.leaf_w = leaf_w
        self.leaf_h = leaf_h
        # self.rep_num = rep_num
        self.point = (0, 0)
        self.c.create_oval(300, 330, 180, 200, width=0, fill='white')
        for n in range(self.rep_num):
            rand = random.random()
        #
        #     if rand < 0.01:
        #         self.point = f1(self.point)  # Отрисовка стебля
        #     elif rand < 0.86:
        #         self.point = f2(self.point)  # Отрисовка меньших листьев
        #     elif rand < 0.93:
        #         self.point = f3(self.point)  # Отрисовка левой части
        #     else:
        #         self.point = f4(self.point)  # Отрисовка правой части
        #
        #     draw_point = W / 2 + (self.leaf_w * self.point[0]), H - (self.leaf_h * self.point[1])
        #     c.create_oval(draw_point, draw_point, width=0, fill='white')
        #
        # root.after(1, self.run(self.leaf_w, self.leaf_h, self.rep_num))


if __name__ == "__main__":
    root = Tk()
    W = 300  # ширина
    H = 380  # высота

    leaf_w = 55  # ширина листка
    leaf_h = 35  # высота листка

    c = Canvas(root, width=W, height=H, bg='#000000')
    # c.pack()

    root.bind('<Escape>', esc)  # Закрыть окно при помощи esc

    # main()

    app = Application(master=root, rep_num=800)
    app.run(leaf_w=55, leaf_h=35)
    app.mainloop()

    # pap = Image(master=root, 55, 35, (0, 0), 800)
    # pap.run()
    # pap.mainloop()
