import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image

# List of image files to use as layers
image_files = [
    'blue-wave-6-layer.png',
    'wave-layer-7-green.png',
    'wave-layer-7-orange.png',
    'wave-layer-7-purple.png',
    'wave-layer-7-red.png',
    'wave-layer-7-water-blue.png'
]

# Load all images once before the animation
loaded_images = [Image.open(image_file).convert("RGBA") for image_file in image_files]

# Create the figure for animation
fig, ax = plt.subplots(figsize=(10, 10), dpi=100)

# Function to create the figure for each frame of the animation
def animate(frame_num):
    ax.clear()  # Clear previous frame
    ax.axis('off')
    
    # Iterate through each loaded image and add it as a layer with varying opacities and blending modes
    for idx, image in enumerate(loaded_images):
        # Convert image to a NumPy array for manipulation
        image_data = np.array(image)

        # Add transparency effect to each layer and add dynamic change for animation
        base_alpha = 0.8 - 0.1 * idx
        dynamic_factor = 0.5 + 0.5 * np.sin(frame_num / 10.0)
        alpha = int(255 * base_alpha * dynamic_factor)
        image_data[..., 3] = alpha

        # Create an Image object from modified array
        modified_image = Image.fromarray(image_data)

        # Display the image as a layer
        ax.imshow(modified_image, interpolation='bilinear')

# Set up the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=100, repeat=True)

# Save the animation as a GIF
animation_path = "wave_layers_animation.gif"
ani.save(animation_path, writer='pillow', fps=20)

plt.close(fig)

print(f"Animation saved as {animation_path}")
