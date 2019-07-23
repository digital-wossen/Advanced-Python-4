# JTSK-350112
# a4 2.py
# Wossen Hailemariam
# w.hailemariam@jacobs-university.de


from graphics import *

def main():
    win = GraphWin("Face", 500,500)
    
    shape1big = Circle(Point(250,250), 250)
    shape1big.setOutline("black")
    shape1big.setFill("purple")
    shape1big.draw(win)
    
    shape1 = Circle(Point(250,250), 100)
    shape1.setOutline("black")
    shape1.setFill("Yellow")
    shape1.draw(win)


    shape2 = Circle(Point(210,220), 20)
    shape2.setOutline("black")
    shape2.setFill("blue")
    shape2.draw(win)
    

    shape3 = shape2.clone()
    shape3.move(80,0)
    shape3.draw(win)

    shape2ear = Oval(Point(135,220),Point(150,280))
    shape2ear.setOutline("black")
    shape2ear.setFill("red")
    shape2ear.draw(win)
    

    shape3ear = shape2ear.clone()
    shape3ear.move(215,0)
    shape3ear.draw(win)

    shape2earring = Circle(Point(125,180), 20)
    shape2earring.setOutline("black")
    shape2earring.setFill("blue")
    shape2earring.draw(win)
    

    shape3earring = shape2earring.clone()
    shape3earring.move(250,0)
    shape3earring.draw(win)

    shape2earr = Circle(Point(80,125), 20)
    shape2earr.setOutline("black")
    shape2earr.setFill("blue")
    shape2earr.draw(win)


    shape3earr = shape2earr.clone()
    shape3earr.move(340,0)
    shape3earr.draw(win)



    shape4 = Circle(Point(250,300), 40)
    shape4.setOutline("black")
    shape4.setFill("black")
    shape4.draw(win)




    pa1 = Point(250,230)
    pa2 = Point(270,250)
    pa3 = Point(230,250)

    triangle1 = Polygon(pa1,pa2,pa3)
    triangle1.setFill("green")
    triangle1.setOutline("cyan")
    triangle1.draw(win)



    if win.getMouse():
        win.close()


main()