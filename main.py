from graphics import Point as pt
from graphics import *
import numpy as np
from numpy import pi

global win
win = GraphWin("test", 600, 600)


def make_star(p1, p2, x, y):
    pt_lst = []
    shift = 1.5 * pi
    for i in range(10):
        if i % 2 == 0:
            pt_lst.append(pt((p1 * np.cos((2 * pi * (i / 2)) / 5 + shift)),
                             (p1 * np.sin((2 * pi * (i / 2)) / 5 + shift))))
        else:
            pt_lst.append(pt((p2 * np.cos((2 * pi * int(i / 2)) / 5 + shift + ((2 * pi) / 10))),
                             (p2 * np.sin((2 * pi * int(i / 2)) / 5 + shift + ((2 * pi) / 10)))))
    # print(pt_lst)
    for i in pt_lst:
        i.x += x
        i.y += y
    return Polygon(pt_lst)


def draw_flag(x, y, w, h):
    r = Rectangle(pt(x, y), pt(x + w, y + h))
    r.setFill("blue")
    c = Circle(pt(x + w / 2, y + h / 2), h / 4)
    c.setFill("yellow")
    s = make_star(0.25 * h, 0.1 * h, x + w / 2, y + h / 2)
    s.setFill("white")
    r.draw(win)
    c.draw(win)
    s.draw(win)


def main():
    draw_flag(150, 200, 300, 200)
    # s = make_star(50, 20, 300, 300)
    # s.draw(win)
    win.getMouse()
    win.close()


main()
