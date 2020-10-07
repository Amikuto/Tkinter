from tkinter import *
from random import *


def circle_color():
    color = choice(['aqua', 'blue', 'fuchsia', 'green', 'maroon', 'orange', \
                    'pink', 'purple', 'red', 'yellow', 'violet', 'indigo', 'chartreuse', 'lime', '#f55c4b'])
    return color


def circle(x0, y0, d):
    if d >= 50:  # Рисовать круги пока диаметр не достигнет этого значения
        if x0 == 0 and y0 == 0:
            color = circle_color()  # Берем случайный цвет для круга
            canvas.create_oval(x0, y0, x0 + d, y0 + d, fill=color, width=1)
            # canvas.create_oval(x0, y0, x0+d, y0+d, outline="red", fill="green", width=2)
        d = d / 2  # Каждый последующий круг с половинным диаметром
        sx = 10  # Смещение по x
        # Вычисление коэффициента смещения кругов по Y
        koeff_d = size_canvas / d  # 2(0), 4(1), 8(3), 16(7), 32(15), 64(31)...
        # Вычисление координаты круга y0 со смещением по Y
        y0 = d / 2 + d * (koeff_d / 2 - 1)
        # y0 = d/2
        x = 0  # Переменная цикла
        color = circle_color()  # Берем случайный цвет для кругов
        while x < 200:  # Цикл, чтобы круга было вписано всегда x (2)
            x0 = (d) * x  # Вычисление координаты круга x0 (их x)
            canvas.create_oval(x0 + sx, y0 + sx, x0 + d - sx, y0 + d - sx, fill=color, width=1)
            root.after(10, root.update())
            #            print ('---x='+str(x))
            #            print ('d='+str(d))
            #            print ('x0='+str(x0))
            #            print ('y0='+str(y0))
            x += 1

        circle(x0, y0, d)  # Вызов рекурсии для создания x кругов, диаметра d в левом круге


size_canvas = 600  # Размер канвы
root = Tk()  # Создаем окно
canvas = Canvas(root, width=size_canvas, height=size_canvas)  # Создаем холст
canvas.pack()  # Указание расположить холст внутри окна
d = size_canvas  # Диаметр круга
x0 = 0  # Начальные точки круга
y0 = 0
circle(x0, y0, d)
root.mainloop()  # Применение изменений в окне