import math
from graphics import *

POINTS = 5
WIDTH, HEIGHT = 300, 200

def main():
    win = GraphWin('Star', 600, 400)
    win.setCoords(-WIDTH, -HEIGHT, WIDTH, HEIGHT)
    win.setBackground('blue')

    vertices = []

    length = min(WIDTH, HEIGHT) / 2

    theta = -math.pi / 2
    delta = 4 / POINTS * math.pi

    for _ in range(POINTS):
        vertices.append(Point(length * math.cos(theta), length * math.sin(theta)))
        # theta += delta
        if POINTS % 2 == 1:
            theta += delta
        else:
            theta += delta / 2

    # Use Polygon object to draw the star
    star = Polygon(vertices)
    star.setFill('darkgreen')
    star.setOutline('lightgreen')
    star.setWidth(4)  # width of boundary line
    star.draw(win)

    for i in range(len(vertices)):
        print(vertices[i])

    win.getMouse()
    win.close()

main()
