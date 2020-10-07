from tkinter import *
from math import log


def esc(event):
    root.destroy()


def main_func(center, z):  # Берем центр и переменную цикла
    """Данная функция принимает центр и от него слева и справа на равноудаленном расстоянии рисует 2 круга"""
    buff = W // z  # Бафферная переменная вычисляющая середину растояния от края до центра

    radius = W / z  # Радиус кругов

    # Определяем центр круга при помощи вычитания от центра круга половину расстояния до края
    new_center = center - buff, H - 250
    c.create_oval(new_center[0] - radius, new_center[1] - radius,
                  new_center[0] + radius, new_center[1] + radius,
                  outline="white")

    # Определяем центр круга при помощи добавления от центра круга половину расстояния до края
    new_center = center + buff, H - 250
    c.create_oval(new_center[0] - radius, new_center[1] - radius,
                  new_center[0] + radius, new_center[1] + radius,
                  outline="white")

    # функция отрисовки кругов в левую сторону
    def into_left(ctr, z):
        ctr = ctr - buff  # От центра отнимаем его половину
        z *= 2  # Переменная для вычисления радиуса и бафферной переменной
        if log(z, 2) <= num:  # Рекурсия будет выполняться пока переменная цикла меньше числа данного пользователем
            main_func(ctr, z)  # Передаем новый центр и переменную цикла в функцию

    # функция отрисовки кругов в правую сторону, аналогична отрисовке в левую
    def into_right(ctr, z):
        ctr = ctr + buff  # От центра УЖЕ прибавляем его половину
        z *= 2
        if log(z, 2) <= num:
            main_func(ctr, z)

    into_left(center, z)
    into_right(center, z)


if __name__ == "__main__":
    root = Tk()

    W = 500  # Width
    H = 500  # Height

    root.bind('<Escape>', esc)  # Закрыть окно при помощи esc

    c = Canvas(root, width=W, height=H, bg='#000000')

    '''Вообще у меня полная рекурсия, которая начинается с двух кругов, 
    но т.к. на примере рекурсия находится в 1 круге я просто обрезаю Canvas на половину
    посмотреть полную рекурсию можно при помощи строки снизу'''
    # c = Canvas(root, width=1000, height=1000, bg='#000000')

    c.pack()

    loop = 2  # Переменная для уменьшения радиуса
    num = int(input("type num of loops: "))  # Ввод пользователем колличества отприсовываемых кругов
    # num = 10

    main_func(W, loop)  # Передаем в функцию центр (в данном случае ширину) и переменную цикла

    root.mainloop()
