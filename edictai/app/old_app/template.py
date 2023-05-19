from PIL import Image, ImageOps

# Load the input image
input_image = Image.open('back.webp')

# Define the thumbnail size and calculate the ratio
thumbnail_size = (1280, 720)
thumbnail_ratio = thumbnail_size[0] / thumbnail_size[1]

# Calculate the new size that maintains the aspect ratio
input_ratio = input_image.size[0] / input_image.size[1]
if input_ratio > thumbnail_ratio:
    new_width = thumbnail_size[0]
    new_height = int(new_width / input_ratio)
else:
    new_height = thumbnail_size[1]
    new_width = int(new_height * input_ratio)

# Resize the image with the new width and height
resized_image = input_image.resize((new_width, new_height))

# Add an aqua-colored border
border_size = int(new_width * 0.02)
border_color = (0, 255, 255) # Aqua color in RGB
border_image = ImageOps.expand(resized_image, border=border_size, fill=border_color)

# Add a light grey background and bottom margin
background_color = (230, 230, 230) # Light grey color in RGB
background_image = Image.new('RGB', thumbnail_size, background_color)
background_image.paste(border_image, (int((thumbnail_size[0] - new_width) / 2), int(thumbnail_size[1] - new_height - (thumbnail_size[1] * 0.2))))

# Save the final thumbnail image
background_image.save('output_image.jpg')
