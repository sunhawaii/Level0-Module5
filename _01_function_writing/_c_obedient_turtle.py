"""
Make an obedient turtle that will obey commands to draw shapes.
"""
from tkinter import messagebox, simpledialog, Tk
import turtle


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    window = turtle.Screen()
    window.bgcolor('white')
    # TODO)
    #   1. Create a turtle.
    turt = turtle.Turtle()
    #   2. Write 3 method definitions for drawing a square, triangle, and
    #      circle.
    def draw_square():
        for i in range(4):
            turt.forward(100)
            turt.left(90)
    def draw_triangle():
        for i in range(3):
            turt.forward(120)
            turt.left(120)
    def draw_circle():
        turt.circle(100)
    #   3. Ask the user for the for a shape to draw.
    shape = simpledialog.askstring(None, prompt= "What shape do you want to draw?")
    #   4. Draw the appropriate shape depending on their answer (call the right
    #      function)
    if shape == 'square':
        draw_square()
    elif shape == 'triangle':
        draw_triangle()
    elif shape == 'circle':
        draw_circle()
    pass
turtle.done