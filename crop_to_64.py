# Filename: crop_to_64.py

from PIL import Image

def crop_to_multiple_of_64(image_path, output_path):
    """
    Crop the input image so that its dimensions are multiples of 64 and save the result.

    Parameters:
    - image_path: str, path to the input image file.
    - output_path: str, path where the cropped image will be saved.
    """
    # Open the image
    img = Image.open(image_path)
    width, height = img.size

    # Calculate new dimensions that are multiples of 64
    new_width = (width // 64) * 64
    new_height = (height // 64) * 64

    # Calculate the coordinates to crop the image
    left = (width - new_width) // 2
    top = (height - new_height) // 2
    right = left + new_width
    bottom = top + new_height

    # Crop the image
    img_cropped = img.crop((left, top, right, bottom))

    # Save the cropped image
    img_cropped.save(output_path)
    print(f"Cropped image saved to {output_path}")

# Example usage
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Crop an image to dimensions that are multiples of 64.")
    parser.add_argument("input", help="Path to the input image file.")
    parser.add_argument("output", help="Path to save the cropped image.")
    args = parser.parse_args()

    crop_to_multiple_of_64(args.input, args.output)
