import matplotlib.pyplot as plt
from tkinter import *
from random import randint


def esc(event):
    root.destroy()


root = Tk()

W = 500  # ширина
H = 500  # высота

root.bind('<Escape>', esc)  # Закрыть окно при помощи esc

c = Canvas(root, width=W, height=H, bg='#000000')

c.pack()

# initializing the list
x = []
y = []

# setting first element to 0
x.append(0)
y.append(0)

current = 0

c.create_oval(x, y, x, y, width=1, fill='white')

for i in range(1, 50000):

    z = randint(1, 100)

    if z == 1:
        x.append(0)
        y.append(0.16 * (y[current]))
        print(x[-1], y[-1])
        # c.create_oval(x[-1], y[-1], x[-1], y[-1], width=0, fill='white')
#
#         # for the probability 0.85
    if z >= 2 and z <= 86:
        x.append(0.85 * (x[current]) + 0.04 * (y[current]))
        y.append(-0.04 * (x[current]) + 0.85 * (y[current]) + 1.6)
#
#         # for the probability 0.07
    if z >= 87 and z <= 93:
        x.append(0.2 * (x[current]) - 0.26 * (y[current]))
        y.append(0.23 * (x[current]) + 0.22 * (y[current]) + 1.6)
#
#         # for the probability 0.07
    if z >= 94 and z <= 100:
        x.append(-0.15 * (x[current]) + 0.28 * (y[current]))
        y.append(0.26 * (x[current]) + 0.24 * (y[current]) + 0.44)

    # c.create_oval(x[current], y[current], x[current], y[current], width=0, fill='white')
    current = current + 1

# plt.scatter(x, y, s=0.2, edgecolor='green')
#
# plt.show()

# print(x, y, sep="\n")

root.mainloop()
