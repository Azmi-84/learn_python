from turtle import *
import colorsys
import math

bgcolor("black")
tracer(0)  # Speed up drawing by not updating every frame
speed(0)
pensize(2)

h = 0.0  # Initial hue for color gradient
num_points = 500  # Number of points (higher for more complexity)
golden_angle = 137.5  # Approximation of the golden angle
rotation_angle = 0  # Initial rotation angle for animation


def draw_dynamic_sunflower(rotation_angle):
    global h
    for i in range(num_points):
        # Fibonacci-based scaling for radius and angle
        r = math.sqrt(i) * 15  # Spiral outwards (sqrt for smooth transition)
        angle = i * golden_angle + rotation_angle  # Add rotation for animation

        # Convert polar to Cartesian coordinates
        x = r * math.cos(math.radians(angle))
        y = r * math.sin(math.radians(angle))

        # Compute the color gradient using HSV model
        c = colorsys.hsv_to_rgb(h, 1, 1)
        h += 0.005  # Faster color transitions for vibrancy
        if h >= 1.0:  # Reset hue to maintain the loop of colors
            h = 0.0
        color(c)

        # Move to the point without drawing, then draw the petal/shape
        up()
        goto(x, y)
        down()

        # Create a vibrant, complex shape with layered petals
        begin_fill()
        fillcolor(c)
        circle(6, steps=8)  # Use octagons for sharper, more vibrant shapes
        end_fill()


def evolve_design():
    global rotation_angle
    clear()  # Clear the previous frame to redraw the new position
    draw_dynamic_sunflower(rotation_angle)
    update()  # Update the screen to show the current frame
    rotation_angle += 1  # Increment rotation to create dynamic evolution


def main():
    """Main loop to continuously evolve the sunflower design."""
    while True:
        evolve_design()


main()
done()
