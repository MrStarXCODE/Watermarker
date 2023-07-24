Image Watermarker
This is a simple script to add a watermark to all images in a specified directory.

Author
$Kek - MrStarXCODE

Installation
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/MrStarXCODE/Watermarker.git
Navigate to the cloned directory:

bash
Copy code
cd your_repo
Install the required Python packages:

bash
Copy code
pip install pillow
Usage
Replace 'imgs' in the script with the path to the directory containing the images you want to watermark.

Replace 'path_to_your_watermark_image.png' in the script with the path to the image you want to use as a watermark.

Run the script:

bash
Copy code
python3 watermark.py
Your watermarked images will be saved in the same directory as the original images with 'watermarked_' prefixed to the original file names.

Customization
You can adjust the size and position of the watermark by modifying the watermark_width and position variables in the script.

