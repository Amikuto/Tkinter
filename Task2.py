from tkinter import *

root = Tk()

# W = root.winfo_screenwidth()
# H = root.winfo_screenheight()
W = 500
H = 500
print(W, H)
cX, cY = W / 2, H / 2

root.attributes('-fullscreen', True)


def esc(event):
    root.destroy()
root.bind('<Escape>', esc)


c = Canvas(root, width=W, height=H, bg='#000000')
c.pack()

radius = H - 250
center = W - 250, H - 250   # Первый арг - координата X, вторая Y

print("Radius = ", radius, "Center = ", center)

oval = c.create_oval(center[0] - radius, center[1] - radius,
                     center[0] + radius, center[1] + radius,
                     outline="white")


radius = H - 400

center = W - 350, H/2
print(center)
c.create_oval(center[0] - radius, center[1] - radius,
              center[0] + radius, center[1] + radius,
              outline="white")

center = W - 150, H/2
print(center)
c.create_oval(center[0] - radius, center[1] - radius,
              center[0] + radius, center[1] + radius,
              outline="white")








































def test(q):
    c.create_oval(center[0] - 20*q - radius / q, center[1] - radius / q,
                  center[0] - 20*q + radius / q, center[1] + radius / q,
                  outline="white")

    c.create_oval(center[0] + 20 * q - radius / q, center[1] - radius / q,
                  center[0] + 20 * q + radius / q, center[1] + radius / q,
                  outline="white")

    c.create_oval(center[0] - radius / q, center[1] + 20 * q - radius / q,
                  center[0] + radius / q, center[1] + 20 * q + radius / q,
                  outline="white")

    c.create_oval(center[0] - radius / q, center[1] - 20 * q - radius / q,
                  center[0] + radius / q, center[1] - 20 * q + radius / q,
                  outline="white")


def test2(q):
    c.create_oval(center[0] - radius / q, center[1] - radius / q,
                  center[0] + radius / q, center[1] + radius / q,
                  outline="white")

    c.create_oval(center[0] - radius / q, center[1] - radius / q,
                  center[0] + radius / q, center[1] + radius / q,
                  outline="white")


x = 1
# while x <= 10:
#     test2(x)
#     x += 1
test2(x)

# print(center)
# print(center[0], center[0] - radius, center[0] - 200, center[0] - 270)
# print(center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius)


x = 200
y = 2.5


def cre_oval(z, q):
    c.create_oval(center[0] - z - radius / q, center[1] - radius / q,
                  center[0] - z + radius / q, center[1] + radius / q,
                  outline="white")

    c.create_oval(center[0] + z - radius / q, center[1] - radius / q,
                  center[0] + z + radius / q, center[1] + radius / q,
                  outline="white")


# cre_oval(x, y)
# x += 70
# y = y * 2.5
# cre_oval(x, y)
# x += 30
# y = y * 2.5
# cre_oval(x, y)

# oval = c.create_oval(center[0]-200 - radius/2.5, center[1] - radius/2.5,
#                      center[0]-200 + radius/2.5, center[1] + radius/2.5,
#                      outline="white")

# oval = c.create_oval(center[0]+200 - radius/2.5, center[1] - radius/2.5,
#                      center[0]+200 + radius/2.5, center[1] + radius/2.5,
#                      outline="white")


# oval = c.create_oval(center[0]-270 - radius/6.25, center[1] - radius/6.25,
#                      center[0]-270 + radius/6.25, center[1] + radius/6.25,
#                      outline="white")
#
# oval = c.create_oval(center[0]+270 - radius/6.25, center[1] - radius/6.25,
#                      center[0]+270 + radius/6.25, center[1] + radius/6.25,
#                      outline="white")


# oval = c.create_oval(center[0]-300 - radius/15.625, center[1] - radius/15.625,
#                      center[0]-300 + radius/15.625, center[1] + radius/15.625,
#                      outline="white")
#
# oval = c.create_oval(center[0]+300 - radius/15.625, center[1] - radius/15.625,
#                      center[0]+300 + radius/15.625, center[1] + radius/15.625,
#                      outline="white")




# print(center[0]/1.6 - radius/4, center[1] - radius/4, center[0]/1.6 + radius/4, center[1] + radius/4)
# print(center[0]-140, center[0]+140)
# print(radius, radius/2.5, radius-250)


root.mainloop()


