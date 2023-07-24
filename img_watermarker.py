from PIL import Image
import os

# Define the directory containing images
directory = 'imgs'

# Define the watermark image
watermark_img_orig = Image.open('logo.png')

# Loop over every file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.jpg') or filename.endswith('.png'):  # You can add more formats if needed
        # Open the image
        img = Image.open(os.path.join(directory, filename))

        # Get the image size
        img_width, img_height = img.size

        # Resize the watermark
        watermark_width = img_width // 4  # 1/4th of the original image width
        watermark_height = int((watermark_width / watermark_img_orig.width) * watermark_img_orig.height)
        watermark_img = watermark_img_orig.resize((watermark_width, watermark_height))

        # Define the position for the watermark (bottom left corner)
        position = (0, img_height - watermark_img.height)

        # Paste the watermark image on the original image
        img.paste(watermark_img, position, watermark_img)

        # Save the watermarked image
        img.save(os.path.join(directory, 'watermarked_' + filename))

print("Watermarking completed!")
