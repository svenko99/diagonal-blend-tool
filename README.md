# 🔲 Dark Light Showcase Tool

This is a simple command-line tool designed for showcasing light and dark modes of websites by overlaying two images with a triangle mask. It utilizes the Python Imaging Library (PIL) for image processing.

## 📝 Examples

![examples](images/animated_examples.gif)

## Usages

### Prerequisites

- Python 3.x
- Pillow library (`pip install Pillow`)

### Both images need to have the same size, otherwise the script won't work!

- I achieve this by using Firefox's tool `Take screenshot` when I right click on a website, and I click `Save visible`.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/svenko99/dark-light-showcase.git
   ```

2. Navigate to the project directory:

   ```bash
   cd dark-light-showcase
   ```

3. Run the script by providing paths to the input images and the desired output path:

   ```bash
   python src/main.py image1.png image2.png output.png
   ```
