from turtle import *
import math
import colorsys

bgcolor("black")
tracer(0)
speed(0)

h = 0.0  # Initial hue for color gradient
phi = (1 + math.sqrt(5)) / 2  # The golden ratio
num_spirals = 30  # Number of spirals/arcs


def draw_golden_spiral():
    global h
    radius = 5
    angle = 0

    for i in range(num_spirals):
        color_change = colorsys.hsv_to_rgb(h, 1, 1)
        h += 0.02
        color(color_change)

        # Draw arcs that grow based on the golden ratio
        circle(radius, 90)  # Draw a quarter circle (arc)

        # Increase the radius by the golden ratio to follow the spiral pattern
        radius *= phi
        right(90)  # Adjust angle for smooth progression


def main():
    """Main loop for drawing the golden spiral."""
    draw_golden_spiral()
    update()
    done()


main()
