# JTSK-350112
# a4 3.py
# Wossen Hailemariam
# w.hailemariam@jacobs-university.de


from graphics import *





def draw_archery(arch):
    win = GraphWin("Archery Target", 700,700)


    p = Point(350,350)
    p.draw(win)


    #circle_white = Circle(Point(350,350),5*width)
    circle_white = Circle(Point(arch[4][0],arch[4][1]), arch[4][2])

    circle_white.setOutline("black")
    circle_white.setFill("white")
    circle_white.draw(win)


    #circle_black = Circle(Point(350,350), 4*width)
    circle_black = Circle(Point(arch[3][0],arch[3][1]), arch[3][2])
    
    circle_black.setOutline("black")
    circle_black.setFill("black")
    circle_black.draw(win)

    

    #circle_blue = Circle(Point(350,350), 3*width)
    circle_blue = Circle(Point(arch[2][0],arch[2][1]), arch[2][2])  
   
    circle_blue.setOutline("black")
    circle_blue.setFill("blue")
    circle_blue.draw(win)

    #circle_red = Circle(Point(350,350), 2*width)
    circle_red = Circle(Point(arch[1][0],arch[1][1]), arch[1][2])
    
    circle_red.setOutline("black")
    circle_red.setFill("red")
    circle_red.draw(win)

    #circle_yellow = Circle(Point(350,350), width)
    circle_yellow = Circle(Point(arch[0][0],arch[0][1]), arch[0][2])
    
    
    circle_yellow.setOutline("black")
    circle_yellow.setFill("Yellow")
    circle_yellow.draw(win)

    p = Point(350,350)
    p.draw(win)

    if win.getMouse():
        win.close()


ar = input()
#ar = [(100,100,15),(100,100,30),(100,100,45),(100,100,60),(100,100,75)]
draw_archery(ar)


    