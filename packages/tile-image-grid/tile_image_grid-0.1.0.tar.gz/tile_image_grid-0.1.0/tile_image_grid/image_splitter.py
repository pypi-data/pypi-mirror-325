#!/usr/bin/env python3

from PIL import Image
import math
import os
import argparse
import sys
from typing import Tuple, Dict, Any

class ImageSplitter:
    def __init__(self, image_path: str, grid_size: int, output_folder: str):
        self.image_path = image_path
        self.grid_size = grid_size
        self.output_folder = output_folder
        self.validate_inputs()

    def validate_inputs(self) -> None:
        """Validate all input parameters before processing."""
        # Check if image exists
        if not os.path.exists(self.image_path):
            raise FileNotFoundError(f"Image file not found: {self.image_path}")

        # Check if N is a perfect square
        if math.sqrt(self.grid_size) % 1 != 0:
            raise ValueError(f"Grid size should be a perfect square. You provided: {self.grid_size}")

        # Create output directory if it doesn't exist
        os.makedirs(self.output_folder, exist_ok=True)

    def get_cell_dimensions(self, image_size: Tuple[int, int]) -> Tuple[int, int]:
        """Calculate dimensions for each cell."""
        width, height = image_size
        grid_dim = int(math.sqrt(self.grid_size))
        return width // grid_dim, height // grid_dim

    def process(self) -> None:
        """Process the image splitting operation."""
        try:
            with Image.open(self.image_path) as img:
                cell_width, cell_height = self.get_cell_dimensions(img.size)
                grid_dim = int(math.sqrt(self.grid_size))

                for row in range(grid_dim):
                    for col in range(grid_dim):
                        self._save_cell(img, row, col, cell_width, cell_height)

        except Exception as e:
            raise RuntimeError(f"Error processing image: {str(e)}")

    def _save_cell(self, img: Image.Image, row: int, col: int, 
                   cell_width: int, cell_height: int) -> None:
        """Save individual cell from the image."""
        left = col * cell_width
        upper = row * cell_height
        right = (col + 1) * cell_width
        lower = (row + 1) * cell_height

        cell_img = img.crop((left, upper, right, lower))
        cell_img_name = f"{row}_{col}.png"
        cell_img_path = os.path.join(self.output_folder, cell_img_name)
        
        cell_img.save(cell_img_path)
        print(f"Saved {cell_img_path}")

def split_image(input_path: str, output_dir: str, grid_size: int) -> Dict[str, Any]:
    """
    Split an image into a grid of smaller images.
    
    Args:
        input_path (str): Path to the input image
        output_dir (str): Directory to save the output images
        grid_size (int): Number of rows/columns in the grid
    
    Returns:
        Dict[str, Any]: Result dictionary containing status and file paths
    """
    # Open the image
    try:
        img = Image.open(input_path)
    except Exception as e:
        raise Exception(f"Failed to open image: {str(e)}")

    # Calculate dimensions for each tile
    width, height = img.size
    tile_width = width // grid_size
    tile_height = height // grid_size

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    tiles = []
    # Split the image into grid_size x grid_size pieces
    for i in range(grid_size):
        for j in range(grid_size):
            # Calculate coordinates for cropping
            left = j * tile_width
            upper = i * tile_height
            right = left + tile_width
            lower = upper + tile_height

            # Crop the image
            tile = img.crop((left, upper, right, lower))
            
            # Save the tile with format matching ImageReconstructor expectations
            tile_path = os.path.join(output_dir, f'{i}_{j}.png')
            tile.save(tile_path)
            tiles.append(tile_path)

    return {
        'status': 'success',
        'tiles': tiles,
        'grid_size': grid_size,
        'original_size': (width, height)
    }

def main():
    parser = argparse.ArgumentParser(description='Split an image into a grid of equal parts.')
    parser.add_argument('image_path', help='Path to the input image')
    parser.add_argument('grid_size', type=int, help='Number of parts to split into (must be a perfect square)')
    parser.add_argument('output_folder', help='Output folder for the split images')
    parser.add_argument('--format', default='png', help='Output format for split images (default: png)')

    args = parser.parse_args()

    try:
        splitter = ImageSplitter(args.image_path, args.grid_size, args.output_folder)
        splitter.process()
        print(f"\nSuccessfully split image into {args.grid_size} parts!")
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main() 