# JTSK-350112
# a4 5.py
# Wossen Hailemariam
# w.hailemariam@jacobs-university.de




from graphics import *


def main():
    win = GraphWin("crapsGAME",600,700)



    #defining coordinates for ease
    # three by three levels


    level_one = 150
    level_two = 300
    level_three = 450   
    level_four = 600
 
    text1 = Text(Point(level_one, level_one), "Value of \nDice One:")
    text1.draw(win)

    text2 = Text(Point(level_two, level_one), "Value of \nDice Two:")
    text2.draw(win)

    text3 = Text(Point(level_three, level_one), "Value of \nDice Three:")
    text3.draw(win)
    #the result text and box
    rec = Rectangle(Point(level_two - 40, level_three - 20),Point(level_two + 40, level_three + 20))
    rec.setFill("green")
    rec.draw(win)
    button = Text(Point(level_two , level_three),"Result:")
    button.draw(win)
    mouse1 = win.getMouse()
    if rec.p1.x < mouse.x < rec.p2.x and rec.p1.y < mouse.y < rec.p2.y
    
    
        ##
        ##
        ##
    recPlay = Rectangle(Point(level_two - 40, level_four - 20),Point(level_two + 40, level_four + 20))
    recPlay.setFill("silver")
    recPlay.draw(win)
    buttonPlay = Text(Point(level_two , level_four),"Play Again")
    buttonPlay.draw(win)
    mouse2 = win.getMouse()
    if recPlay.p1.x < mouse.x < recPlay.p2.x and recPlay.p1.y < mouse.y < recPlay.p2.y
        ##call game again
        #
        #

    recExit = Rectangle(Point(level_three - 40, level_four - 20),Point(level_three + 40, level_four + 20))
    recExit.setFill("silver")
    recExit.draw(win)
    buttonExit = Text(Point(level_three , level_four),"Exit")
    buttonExit.draw(win)
    mouse3 = win.getMouse() 
    if recExit.p1.x < mouse.x < recExit.p2.x and recExit.p1.y < mouse.y < recExit.p2.y
        win.close()




  




main()