import click
from .processor import ImageProcessor

@click.group()
def cli():
    """Tile Image Grid - Image processing utilities"""
    pass


@cli.command()
@click.argument('input_path')
@click.option('--output-dir', '-o', default='output', help='Output directory')
@click.option('--grid-size', '-g', default=3, help='Grid size')
def split(input_path: str, output_dir: str, grid_size: int):
    """Split an image into a grid"""
    processor = ImageProcessor()
    try:
        result = processor.split_image(
            input_path=input_path,
            output_dir=output_dir,
            grid_size=grid_size
        )
        click.echo(f"Images saved to {result['output_dir']}")
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)

@cli.command()
@click.argument('input_folder')
@click.argument('output_path')
@click.option('--border-thickness', '-b', default=2, help='Border thickness in pixels')
@click.option('--border-color', '-c', nargs=3, type=int, default=(0, 0, 0), help='Border color in RGB (default: 0 0 0)')
def reconstruct(input_folder: str, output_path: str, border_thickness: int, border_color: tuple):
    """Reconstruct an image from tiles in a folder"""
    processor = ImageProcessor()
    try:
        result = processor.reconstruct_image(
            input_folder=input_folder,
            output_path=output_path,
            border_thickness=border_thickness,
            border_color=border_color
        )
        click.echo(f"Reconstructed image saved to {result['output_path']}")
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)

def main():
    cli()

if __name__ == '__main__':
    main() 