from PIL import Image, ImageDraw, ImageFont
import os

# Define the directory containing images
directory = 'imgs'

# Define the watermark text
watermark_text = 'Your Watermark'

# Define the font for the watermark text (you may need to change the font path)
font = ImageFont.truetype('DejaVu_Sans\DejaVuSans-Bold.ttf', 15)

# Loop over every file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.jpg') or filename.endswith('.png'):  # You can add more formats if needed
        # Open the image
        img = Image.open(os.path.join(directory, filename))

        # Set up a drawing context
        draw = ImageDraw.Draw(img)

        # Get the image size
        img_width, img_height = img.size

        # Define the position of the watermark text
        position = (10, img_height-20)  # adjust the second value if you want to move the watermark up or down

        # Apply the watermark
        draw.text(position, watermark_text, font=font, fill='white')

        # Save the watermarked image
        img.save(os.path.join(directory, 'watermarked_' + filename))

print("Watermarking completed!")
