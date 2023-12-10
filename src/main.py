import os
import argparse

from PIL import Image, ImageDraw


def overlay_images(image_path1, image_path2, output_path):
    # Open the two images
    image1 = Image.open(image_path1)
    image2 = Image.open(image_path2)

    # Ensure both images have the same size
    if image1.size != image2.size:
        raise ValueError("Both images must have the same dimensions")

    # Create a mask for the right triangle with a diagonal from bottom-left to top-right
    width, height = image1.size
    mask = Image.new("L", (width, height), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.polygon([(0, 0), (width, 0), (0, height)], fill=255)

    # Apply the mask to image1
    image1.putalpha(mask)

    # Paste image1 onto image2 starting from the top-left corner
    image2.paste(image1, (0, 0), image1)

    # Save the result
    image2.save(output_path)


def main():
    parser = argparse.ArgumentParser(
        description="Overlay two images with a triangle mask."
    )
    parser.add_argument("image1", help="Path to the first image")
    parser.add_argument("image2", help="Path to the second image")
    parser.add_argument("output", help="Path to save the result")

    args = parser.parse_args()

    # Convert relative paths to absolute paths
    image1_path = os.path.abspath(args.image1)
    image2_path = os.path.abspath(args.image2)
    output_path = os.path.abspath(args.output)
    try:
        overlay_images(image1_path, image2_path, output_path)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
