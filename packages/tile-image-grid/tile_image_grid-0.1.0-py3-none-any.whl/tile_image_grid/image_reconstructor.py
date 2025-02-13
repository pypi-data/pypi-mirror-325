#!/usr/bin/env python3



from PIL import Image
import os
import argparse
import sys
from typing import Tuple, List, Dict, Any
import math
import json
import torch
from diffusers import StableDiffusionPipeline

class ImageReconstructor:
    def __init__(self, input_folder: str, output_path: str, border_thickness: int = 2, border_color: Tuple[int, int, int] = (0, 0, 0)):
        self.input_folder = input_folder
        self.output_path = output_path
        self.border_thickness = border_thickness
        self.border_color = border_color
        self.validate_inputs()

    def validate_inputs(self) -> None:
        """Validate input parameters."""
        if not os.path.exists(self.input_folder):
            raise FileNotFoundError(f"Input folder not found: {self.input_folder}")
        
        if not os.path.isdir(self.input_folder):
            raise NotADirectoryError(f"Input path is not a directory: {self.input_folder}")

    def get_image_files(self) -> List[str]:
        """Get sorted list of image files from input folder."""
        files = [f for f in os.listdir(self.input_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
        # Sort files by row and column numbers
        return sorted(files, key=lambda x: tuple(map(int, os.path.splitext(x)[0].split('_'))))

    def get_grid_dimensions(self, image_files: List[str]) -> Tuple[int, int]:
        """Calculate grid dimensions based on number of images."""
        n = len(image_files)
        grid_size = int(math.sqrt(n))
        return grid_size, grid_size

    def process(self) -> None:
        """Process the image reconstruction."""
        try:
            image_files = self.get_image_files()
            if not image_files:
                raise ValueError("No image files found in input folder")

            # Get dimensions from first image
            first_image_path = os.path.join(self.input_folder, image_files[0])
            with Image.open(first_image_path) as img:
                cell_width, cell_height = img.size

            grid_rows, grid_cols = self.get_grid_dimensions(image_files)

            # Calculate final image size including borders
            total_width = (cell_width * grid_cols) + (self.border_thickness * (grid_cols + 1))
            total_height = (cell_height * grid_rows) + (self.border_thickness * (grid_rows + 1))

            # Create new image with border color background
            final_image = Image.new('RGB', (total_width, total_height), self.border_color)

            # Place each cell image
            for idx, filename in enumerate(image_files):
                row = idx // grid_cols
                col = idx % grid_cols

                # Calculate position including borders
                x = col * (cell_width + self.border_thickness) + self.border_thickness
                y = row * (cell_height + self.border_thickness) + self.border_thickness

                with Image.open(os.path.join(self.input_folder, filename)) as cell_img:
                    final_image.paste(cell_img, (x, y))

            # Save the final image
            final_image.save(self.output_path)
            print(f"Successfully reconstructed image saved to: {self.output_path}")

        except Exception as e:
            raise RuntimeError(f"Error reconstructing image: {str(e)}")

def reconstruct_image(prompt: str, output_path: str, model: str = 'default', num_steps: int = 50) -> Dict[str, Any]:
    """
    Reconstruct an image from a text prompt.
    
    Args:
        prompt (str): Text prompt describing the desired image
        output_path (str): Path where the output image should be saved
        model (str): Name of the model to use for reconstruction
        num_steps (int): Number of steps in the reconstruction process
    
    Returns:
        Dict[str, Any]: Result dictionary containing status and output path
    """
    # This is a placeholder. You'll need to implement your actual image
    # reconstruction logic here, possibly using a machine learning model
    
    # For now, let's create a simple colored image as a placeholder
    img = Image.new('RGB', (512, 512), color='white')
    
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    
    # Save the image
    img.save(output_path)
    
    return {
        'status': 'success',
        'output_path': output_path,
        'model_used': model,
        'steps_taken': num_steps,
        'prompt': prompt
    }

def main():
    parser = argparse.ArgumentParser(description='Reconstruct a grid of images into a single image with borders.')
    parser.add_argument('input_folder', help='Folder containing the split images')
    parser.add_argument('output_path', help='Path for the output reconstructed image')
    parser.add_argument('--border-thickness', type=int, default=2, help='Thickness of grid borders in pixels (default: 2)')
    parser.add_argument('--border-color', nargs=3, type=int, default=[0, 0, 0],
                        help='Border color in RGB format (default: 0 0 0 for black)')

    args = parser.parse_args()

    try:
        reconstructor = ImageReconstructor(
            args.input_folder,
            args.output_path,
            args.border_thickness,
            tuple(args.border_color)
        )
        reconstructor.process()
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    # Get arguments from command line
    prompt = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else "output.png"
    model = sys.argv[3] if len(sys.argv) > 3 else "CompVis/stable-diffusion-v1-4"
    num_steps = sys.argv[4] if len(sys.argv) > 4 else "50"
    
    reconstruct_image(prompt, output_path, model, num_steps) 