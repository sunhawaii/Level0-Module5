"""
Have the turtle draw a row of houses.
"""
import turtle
from tkinter import messagebox, simpledialog, Tk

def draw_pointy_roof():
    turt.begin_fill()
    turt.fillcolor('brown')

    for n in range(3):
        turt.
    turt.

def draw_house(house_size):
    turt.fillcolor('red')
    turt.begin_fill()
    if house_size == 'small':
        x = 60


        for i in range(4):
            turt.pendown()
            turt.forward(x)
            turt.left(90)
        turt.end_fill()
        turt.fillcolor('green')
        turt.begin_fill()
        turt.forward(x)
        turt.forward(x)
        turt.right(90)
        turt.forward(x/3)
        turt.right(90)
        turt.forward(3*x)
        turt.right(90)
        turt.forward(x/3)
        turt.right(90)
        turt.forward(2*x)
        turt.forward(x*2)
        turt.end_fill()

    if house_size == 'medium':
        x = 120
        for i in range(4):
            turt.pendown()
            turt.fillcolor('red')
            turt.begin_fill()
            turt.forward(x)
            turt.left(90)
        turt.end_fill()
        turt.fillcolor('green')
        turt.begin_fill()
        turt.forward(x)
        turt.right(90)
        turt.forward(x/3)
        turt.right(90)
        turt.forward(3*x)
        turt.right(90)
        turt.forward(x/3)
        turt.right(90)
        turt.forward(2*x)
        turt.end_fill()

    if house_size == 'large':
        x = 120
        for i in range(4):
            turt.pendown()
            turt.fillcolor('red')
            turt.begin_fill()
            turt.forward(x)
            turt.left(90)
        turt.end_fill()
        turt.fillcolor('green')
        turt.begin_fill()
        turt.forward(x)
        turt.right(90)
        turt.forward(x / 3)
        turt.right(90)
        turt.forward(3 * x)
        turt.right(90)
        turt.forward(x / 3)
        turt.right(90)
        turt.forward(2 * x)
        turt.end_fill()

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    window = turtle.Screen()
    window.bgcolor('white')
    turt=turtle.Turtle()

    turt.speed(0)
    turt.penup()
    turt.goto(-300,-300)
    for i in range(10):

        draw_house('small')
    # TODO)
    #   1) Move the turtle to the left side of the window near the bottom.
    #   2) Draw ONE flat-topped house with height=100 and green grass after it.
    #   3) Put the code that drew the house into a function called draw_house
    #      HINT: Only the code that draws one house should go in this function.
    #   4) Using the function you just created, draw 10 houses.
    #      HINT: Use a for loop.
    #   5) Run the code to make sure it works before proceeding.
    #   6) Now change the draw_house function to take height as a parameter.
    #   7) Use random numbers to draw 9 houses of different heights.
    #   8) Run the code to make sure it works before proceeding.
    #   9) Make the draw_house function's height input a string and set the
    #      height of the house based on the following:
    #         “small”            =  60
    #         “medium”           =  120
    #         “large”            =  250
    #   10) Make two new functions that draw different shaped roofs
    #      (JUST the roof part): draw_pointy_roof, draw_flat_roof
    #   11) By calling the correct "roof" function, make large houses have
    #      flat roofs and all the others have pointy roofs.
    pass
