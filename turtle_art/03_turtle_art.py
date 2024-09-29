from turtle import *
import colorsys
import random
import time

bgcolor("black")
tracer(0)
screensize(10000, 10000)

h = 0.0
speed(0)
pensize(2)


def draw_spiral_fractal(x, y, size, angle_offset):
    """Draws a spiral fractal pattern with random properties."""
    global h
    up()
    goto(x, y)
    down()
    color_change_rate = 0.005
    for i in range(200):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        color(c)
        h += color_change_rate
        forward(size)
        right(121 + angle_offset)
        circle(i, 50)


def expanding_circle(radius, steps):
    """Draws expanding circles that evolve into more complex shapes."""
    global h
    for i in range(steps):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        color(c)
        h += 0.02
        circle(radius + i * 2)
        right(360 / steps + random.randint(-15, 15))


def animated_organic_growth():
    """Generates continuously evolving artwork that appears to grow organically."""
    global h
    for _ in range(20):
        # Randomly generate evolving fractals and circle spirals in different areas
        x = random.randint(-400, 400)
        y = random.randint(-400, 400)
        size = random.randint(10, 40)
        angle_offset = random.randint(-10, 10)
        draw_spiral_fractal(x, y, size, angle_offset)
        expanding_circle(random.randint(50, 150), random.randint(10, 30))
        update()
        time.sleep(0.1)  # Delay for smooth transitions


def main():
    """Main function to kick off the dynamic pattern evolution."""
    while True:
        animated_organic_growth()


main()
done()
