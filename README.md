
# Image Watermarker

This is a simple script to add a watermark to all images in a specified directory.

## Author

`$Kek - MrStarXCODE`

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/MrStarXCODE/Watermarker.git
   ```
   
2. Navigate to the cloned directory:

   ```bash
   cd your_repo
   ```

3. Install the required Python packages:

   ```bash
   pip install pillow
   ```

## Usage

1. Replace `'imgs'` in the script with the path to the directory containing the images you want to watermark.

2. Replace `'path_to_your_watermark_image.png'` in the script with the path to the image you want to use as a watermark.

3. Run the script:

   ```bash
   python3 watermark.py
   ```

Your watermarked images will be saved in the same directory as the original images with 'watermarked_' prefixed to the original file names.

## Customization

You can adjust the size and position of the watermark by modifying the `watermark_width` and `position` variables in the script.

