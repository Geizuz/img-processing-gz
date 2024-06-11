import cv2
import numpy as np

def blend_images(background_img_path, overlay_img_path, alpha):
    """
    Blend two images with an arbitrary transparency level.

    Parameters:
        background_img (numpy.ndarray): The background image (BGR format).
        overlay_img (numpy.ndarray): The overlay image (BGR format).
        alpha (float): Transparency level between 0.0 (fully transparent) and 1.0 (fully opaque).

    Returns:
        numpy.ndarray: The blended image (BGR format).
    """
    # Load background and overlay images
    background_img = cv2.imread(background_img_path)
    overlay_img = cv2.imread(overlay_img_path, cv2.IMREAD_UNCHANGED)
    
    # Resize background image to match overlay image if needed using lanczos algorithm
    if background_img.shape[:2] != overlay_img.shape[:2]:
        background_img = cv2.resize(background_img, (overlay_img.shape[1], overlay_img.shape[0]), interpolation=cv2.INTER_LANCZOS4)

    # Perform blending
    blended_img = cv2.addWeighted(background_img, 1 - alpha, overlay_img, alpha, 0)

    return blended_img

# Example usage
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Blend two images with an abritrary alpha level.")
    parser.add_argument("input", help="Path to the input image file.")
    parset.add_argument("overlay", help="Path to the overlay image.")
    parser.add_argument("alpha", help="Alpha level for transparency (0-1.0)".)
    parser.add_argument("output", help="Path to save the blended images.")
    args = parser.parse_args()

    # Blend images
    blended_img = blend_images(args.input, args.overlay, args.alpha)

    # Save blended image
    blended_img.save(args.output)
    print(f"Cropped image saved to {args.output}")
