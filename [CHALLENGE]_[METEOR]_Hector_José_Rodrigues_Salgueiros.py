from PIL import Image
import numpy as np

# Open imagem, convert to RGB mode to ensure proper comparison
image = Image.open("meteor_challenge_01.png").convert("RGB")

# Convert to numpy array again
image_data = np.array(image)

# Define RGB color values for each element
red_pixel = (255, 0, 0)    # meteors
white_pixel = (255, 255, 255)  # stars
blue_pixel = (0, 0, 255)   # water

# Identify positions of each element
meteor_positions = np.all(image_data == red_pixel, axis=-1)
star_positions = np.all(image_data == white_pixel, axis=-1)
water_positions = np.all(image_data == blue_pixel, axis=-1)

# Count total stars and meteors
total_stars = np.sum(star_positions)
total_meteors = np.sum(meteor_positions)

# Get the indices of all meteors
meteor_indices = np.argwhere(meteor_positions)

# Count how many meteors fall on water (perpendicular downward path)
meteors_on_water = 0
for x, y in meteor_indices:
    # Start checking downward from the meteor position to see if it hits water
    while x < image_data.shape[0]:
        if water_positions[x, y]:
            meteors_on_water += 1
            break
        x += 1

# Results
print(f"Number of Stars: {total_stars}")
print(f"Number of Meteors: {total_meteors}")
print(f"Meteors falling on the Water: {meteors_on_water}")
