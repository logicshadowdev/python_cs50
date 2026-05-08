import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("black")
s.title("Rainbow Spiral")
t.speed(0)
t.width(2)

h = 0
for i in range(300):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.color(c)
    t.forward(i * 1.0)
    t.left(91)
    h += 1/300

turtle.done()
