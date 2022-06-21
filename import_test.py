from graphics import *

win = GraphWin('Import Test', 400, 400)
win.setBackground('blue')
star_image_gif = Image(Point(200, 200), "star.gif")
star_image_gif.draw(win)
win.getMouse()
star_image_gif.undraw()
star_image_png = Image(Point(200, 200), "star.png")
star_image_png.draw(win)
win.getMouse()
star_image_png.undraw()
# the tkinter documentation says that it supports jpg, however the line below
# fails with the message: _tkinter.TclError: couldn't recognize data in image file "star.jpg"
# star_image_jpg = Image(Point(200, 200), "star.jpg")
# star_image_jpg.draw(win)
win.getMouse()
win.close()
