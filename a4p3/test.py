from graphics import *

win=GraphWin(500,500)






def draw_target(): 
    #draw the target
    rad = 200
    color = ['yellow','white', 'black', 'blue', 'red']
    for i in range(5):
        for j in range(2):
            c = Circle(draw_archery[j], rad)
            c.setFill(color[i])
            c.setOutline('black')
            c.setWidth('2')
            c.draw(win)
            rad = (rad - 19)


if _name_ == '_main_':
    draw_target()



draw_archery=[(100, 100, 15), (100, 100, 30),(100, 100, 45),\
     (100, 100, 60), (100, 100, 75)]