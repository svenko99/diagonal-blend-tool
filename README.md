# 🔲 Diagonal Blend Tool

This is a simple command-line tool designed to blend two images along a diagonal axis.
Its creation was inspired by the desire to showcase both the dark and light modes of my website within a single image.

## 📝 Examples

![examples](images/animated_example2.gif)

## 📊 Usage

### Prerequisites

- Python 3.x
- Pillow library (`pip install Pillow`)

### Both images need to have the same size, otherwise the script won't work!

- I achieve this by using Firefox's tool `Take screenshot` when I right click on a website, and I click `Save visible`. I take a screenshot when the website is in light mode, and then another one when the website is in dark mode.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/svenko99/diagonal-blend-tool.git
   ```

2. Navigate to the project directory:

   ```bash
   cd diagonal-blend-tool
   ```

3. Run the script by providing paths to the input images and the desired output path:

   ```bash
   python src/main.py image1.png image2.png output.png
   ```

## 🔄 Update
- After further searching, I [found](https://bytefreaks.net/applications/imagemagick/imagemagick-collage-merge-two-images-diagonally) a way to achieve the same result using only [ImageMagick](https://imagemagick.org/index.php).
- Here is the revised code:
  
  ```bash
   # Set default filenames
   LEFT=${1:-"image1.png"}
   RIGHT=${2:-"image2.png"}
   OUT="diagonal_blend.png"
   
   # Read image dimensions
   DIMENSIONS=$(identify -format %wx%h "$LEFT")
   WIDTH=${DIMENSIONS%x*}
   HEIGHT=${DIMENSIONS#*x}
   
   # ImageMagick commands to merge images diagonally without intermediate files
   convert -respect-parenthesis \
   \( "$LEFT" -gravity north -crop "$WIDTH"x"$HEIGHT"+0+0 +repage \) \
   \( "$RIGHT" -gravity east -crop "$WIDTH"x"$HEIGHT"+0+0 +repage \) \
   \( -size "$WIDTH"x"$HEIGHT" xc:black -fill white -draw "polygon 0,0 0,$HEIGHT $WIDTH,0" \) \
   \( -clone 2 -negate \) \
   \( -clone 0 -clone 2 -alpha off -compose copy_opacity -composite \) \
   \( -clone 1 -clone 3 -alpha off -compose copy_opacity -composite \) \
   -delete 0-3 -compose over -composite "$OUT"
  ```
