from graphics import *

WINDOW_WIDTH, WINDOW_HEIGHT = 1100, 900

win = GraphWin("Dice GAME", WINDOW_WIDTH, WINDOW_HEIGHT)

def buttons():
   
    play_again = Rectangle(Point(85, 116), Point(115, 146),"Play Again")
    quit = Rectangle(Point(1000, 850), Point(1030, 890), "Quit")

    play_again.setFill("blue")
    quit.setFill("blue")
    #text = Text(Point(100, 133), "Exit")
    #text.draw(win)

    play_again.draw(win)
    quit.draw(win)

    return play_again, quit

def inside(point, rectangle):
    """ Is point inside rectangle? """

    ll = rectangle.getP1()  # assume p1 is ll (lower left)
    ur = rectangle.getP2()  # assume p2 is ur (upper right)

    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()

left, right, quit = buttons()

centerPoint = Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
text = Text(centerPoint, "")
text.draw(win)

while True:
    clickPoint = win.getMouse()

    if clickPoint is None:  # so we can substitute checkMouse() for getMouse()
        text.setText("")
    elif inside(clickPoint, left):
        text.setText("left")
    elif inside(clickPoint, right):
        text.setText("right")
    elif inside(clickPoint, quit):
        break
    else:
        text.setText("")

win.close()