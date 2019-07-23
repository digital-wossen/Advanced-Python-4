# JTSK-350112
# a4 4.py
# Wossen Hailemariam
# w.hailemariam@jacobs-university.de


from graphics import *

def perimeter_rec(leng,wid):
    return 2*(leng + wid)


def area_rec(leng,wid):
    return leng*wid


def main():
    win = GraphWin("Draw RECTANGLE",500,500)

    Text ( Point (400 ,400) , "Area:"). draw ( win )
    Text ( Point (400 ,420) , "Perimeter:"). draw ( win )

    p1 = win.getMouse()
    p1x = p1.getX()
    p1y = p1.getY()

    p2 = win.getMouse()
    p2x = p2.getX()
    p2y = p2.getY()

    p1 = Point(p1x,p1y)
    p2 = Point(p2x,p1y)
    p3 = Point(p1x,p2y)
    p4 = Point(p2x,p2y)
    shape = Polygon(p1, p2, p4, p3)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)


    length =abs(p2x - p1x)
    width = abs(p2y - p1y)

    area = area_rec(length,width)
    perimeter = perimeter_rec(length,width)


    Text ( Point (450 ,400) , area). draw ( win )
    Text ( Point (450 ,420) , perimeter). draw ( win )

    #printing also on the bash
    print("Area:", area)
    print("Perimeter:", perimeter)    
    
    
 
    #click the window third time inorder to close it  
    if win.getMouse():
        win.close()

main()


#print(area_rec(length,width))
#print(perimeter_rec(length,width))
