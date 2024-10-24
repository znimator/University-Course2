import turtle
import random

def draw_tree(turtle, branch_length, angle, shrink_factor, min_length):
    if branch_length < min_length:
        return
    turtle.forward(branch_length)
    turtle.left(angle)
    draw_tree(turtle, branch_length * shrink_factor, angle, shrink_factor, min_length)
    turtle.right(angle * 2)
    draw_tree(turtle, branch_length * shrink_factor, angle, shrink_factor, min_length)
    turtle.left(angle)
    turtle.backward(branch_length)

def main():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.left(90)
    draw_tree(t, 100, 30, 0.7, 5)
    turtle.done()

if __name__ == "__main__":
    main()