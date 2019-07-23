from graphics import *


def calculate(num1, num2, opr):
    
:
    try:   
        if opr == '+':
            return num1 + num2
        elif opr == '-':
            return num1 - num2
        elif opr == '*':
            return num1 * num2
        elif opr = '/':
            return num1 / num2
    except TypeError as exc:
        print("TypeError:", exc)
    except ZeroDivisionError as exc:
        print("ZeroDivisionError:", exc)




def calculator_display():
    win = GraphWin("Calculator", 900,700)

    #defining coordinates for ease
    # three by three levels


    level_one = 200
    level_two = 400
    level_three = 600    

    #start from the text files

    text1 = Text(Point(level_one, level_one), "First Number")
    text1.draw(win)

    text2 = Text(Point(level_two, level_one), "Operation")
    text2.draw(win)

    text3 = Text(Point(level_three, level_one), "Second Number")
    text3.draw(win)



    #second line --- inputs
  
    inputone = Entry(Point(level_one,level_two),5)
    inputone.setText("0.0")
    inputone.draw(win)


    inputsec = Entry(Point(level_three,level_two),5)
    inputsec.setText("0.0")
    inputsec.draw(win)
  

    inputope = Entry(Point(level_two,level_two),10)
    inputope.setText("")
    inputope.draw(win)
    oprec = Rectangle(Point(level_two - 40, level_two - 20),Point(level_two + 40, level_two + 20))
    oprec.setFill("black")
    oprec.draw(win)

    #third line 


    #exit button
    exrec = Rectangle(Point(level_one - 40, level_three - 20),Point(level_one + 40, level_three + 20))
    exrec.setFill("silver")
    exrec.draw(win)

    button2 = Text(Point(level_one , level_three),"Exit")
    button2.draw(win)
   
    #result button and result output

    rec = Rectangle(Point(level_two - 40, level_three - 20),Point(level_two + 40, level_three + 20))
    rec.setFill("blue")
    rec.draw(win)
    button = Text(Point(level_two , level_three),"Result:")
    button.draw(win)
    while True:
        mouseResult = win.getMouse()
        if rec.p1.x < mouseResult.x < rec.p2.x and rec.p1.y < mouseResult.y < rec.p2.y:
            resulttext = calculate(inputone,inputsec,inputope)

            output = Text(Point(level_three, level_three),"")
            output.draw(win)
            output.setText(resulttext)

            if exrec.p1.x < mouseResult.x < exrec.p2.x and exrec.p1.y < mouseResult.y < exrec.p2.y:
                win.close()

    #mouseExit = win.getMouse()
    #if exrec.p1.x < mouseExit.x < exrec.p2.x and exrec.p1.y < mouseExit.y < exrec.p2.y:
     #   win.close()



    
