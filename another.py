import tkinter
import math


def esc(event):
    root.destroy()


def stick(point, angle, length):
    if length < minLength:
        return

    # Вычислим и приведем углы к промежутку от 0 до 360 градусов
    lb_angle = toAngle(angle + angleBetweenSticks)
    rb_angle = toAngle(angle - angleBetweenSticks)

    x, y = point[0], point[1]
    # Получим точки в которые нужно провести линии
    left = getEndPoint(x, y, lb_angle, length)
    right = getEndPoint(x, y, rb_angle, length)

    # Узнаем насколько близко длина новых палок к минимальной
    # и в соответствии с этим зададим толщину линий
    stick_w = 10 * ((length - minLength) / (startLength - minLength))
    c.create_line(x, y, left[0], left[1], width=stick_w, fill='black')
    c.create_line(x, y, right[0], right[1], width=stick_w, fill='black')

    # Рекурсивно генерируем следующие ветки
    stick(left, lb_angle, length * lenFactor)
    stick(right, rb_angle, length * lenFactor)


# кортеж с точками конца
def getEndPoint(x, y, angle, length):
    return (
        x - (math.sin(math.radians(angle)) * length),
        y - (math.cos(math.radians(angle)) * length))


def toAngle(angle):
    while angle < 0:
        angle += 360
    while angle >= 360:
        angle -= 360
    return angle


if __name__ == '__main__':

    angleBetweenSticks = 30  # Угол
    lenFactor = 0.8  # Множитель длины
    startLength = 100  # Начальная длина
    minLength = 5  # Минимальная длина после прекращения

    root = tkinter.Tk()
    width, height = 1000, 500
    c = tkinter.Canvas(root, width=width, height=height)
    c.pack()

    root.bind('<Escape>', esc)

    x = width/2
    y = height

    root_x = width / 2
    root_y = height // 2
    c.create_line(root_x, root_y, x, y, fill='black', width=10)

    stick((root_x, root_y), 0, startLength * lenFactor)
    root.mainloop()
