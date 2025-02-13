import os
from typing import Dict, Any, Optional

class ImageProcessor:
    def __init__(self):
        pass
        
    def reconstruct_image(self, 
                         input_folder: str,
                         output_path: str,
                         border_thickness: int = 2,
                         border_color: tuple = (0, 0, 0)) -> Dict[str, Any]:
        """
        Reconstruct an image from tiles in a folder
        
        Args:
            input_folder (str): Path to folder containing image tiles
            output_path (str): Path where reconstructed image will be saved
            border_thickness (int): Thickness of borders between tiles
            border_color (tuple): RGB color tuple for borders
            
        Returns:
            Dict[str, Any]: Result dictionary containing status and output path
        """
        from .image_reconstructor import ImageReconstructor
        
        reconstructor = ImageReconstructor(
            input_folder=input_folder,
            output_path=output_path,
            border_thickness=border_thickness,
            border_color=border_color
        )
        
        reconstructor.process()
        
        return {
            'status': 'success',
            'output_path': output_path
        }

    def split_image(self,
                    input_path: str,
                    output_dir: str = 'output',
                    grid_size: int = 3) -> Dict[str, Any]:
        """
        Split an image into a grid
        """
        from .image_splitter import split_image
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        result = split_image(
            input_path=input_path,
            output_dir=output_dir,
            grid_size=grid_size
        )
        
        return {
            'output_dir': output_dir,
            'status': 'success'
        } 