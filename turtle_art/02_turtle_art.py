from turtle import *
import colorsys
import random

bgcolor("black")
tracer(0)
screensize(10000, 10000)

h = 0
speed(0)
pensize(2)


def draw_fractal():
    global h
    up()
    goto(random.randint(-400, 400), random.randint(-400, 400))
    down()
    for i in range(250):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        color(c)
        h += 0.005
        forward(i * 2)
        right(121)
        circle(i, 200)


def dynamic_circle_pattern(radius, steps):
    global h
    up()
    goto(0, 0)
    down()
    for i in range(steps):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        color(c)
        h += 0.02
        circle(radius)
        right(360 / steps + random.randint(-10, 10))


def main():
    for _ in range(10):
        draw_fractal()
        dynamic_circle_pattern(random.randint(
            100, 300), random.randint(20, 50))
        update()


main()
done()
