import tkinter as tk
import math


def move_func():
    coords[0] += 2*speed
    print(coords[0])

    start_x, start_y = center
    distance = 200
    angle = coords[0]

    x = start_x - distance * math.sin(math.radians(-angle))
    y = start_y - distance * math.cos(math.radians(-angle))

    x_1 = x - radius
    y_1 = y - radius
    x_2 = x + radius
    y_2 = y + radius

    c.coords(obj_number, x_1, y_1, x_2, y_2)
    root.after(1, move_func)


def esc(event):
    root.destroy()


root = tk.Tk()
c = tk.Canvas(root, width=600, height=600, bg="white")
c.pack()
root.bind('<Escape>', esc)

radius = 200
center = 300, 300  # Первый арг - координата X, вторая Y
c.create_oval(center[0] - radius, center[1] - radius,
              center[0] + radius, center[1] + radius,
              fill="orange")

radius = 10
center = 300, 300  # Первый арг - координата X, вторая Y
obj_number = c.create_oval(center[0] - radius, center[1] - radius,
                           center[0] + radius, center[1] + radius,
                           fill="black")

speed = 0.05
coords = [0]
move_func()

root.mainloop()
