from turtle import *
import math
import colorsys

bgcolor("black")
tracer(0)
speed(0)

h = 0.0  # Initial hue for color gradient

# Parameters for the Lissajous curve
a = 5  # Frequency along the x-axis
b = 6  # Frequency along the y-axis
delta = math.pi / 2  # Phase shift


def draw_lissajous_curve(num_points=1000, scale=200):
    global h
    for t in range(num_points):
        # Calculate the x and y positions based on sine functions
        x = scale * math.sin(a * t * 0.01 + delta)
        y = scale * math.sin(b * t * 0.01)

        color_change = colorsys.hsv_to_rgb(h, 1, 1)
        h += 0.001
        color(color_change)

        # Draw the curve using small line segments
        up()
        goto(x, y)
        down()
        dot(3)  # Draw a small dot to make the curve smooth


def main():
    """Main loop to draw the Lissajous curve."""
    draw_lissajous_curve()
    update()
    done()


main()
